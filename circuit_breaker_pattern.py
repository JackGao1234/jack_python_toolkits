from datetime import datetime, timedelta
import time


"""
Sometimes, we don't want to retry if the function failed once
We'd like to wait for a while. Retry later

e.g. 
There's a web service unstable for a while.
You don't want to over-hit it and waste computing time
because it seems impossible to restored within few seconds
"""


def circuit_breaker_decorator_factory(breaker):
    """input: any circuit breaker which has methods guard(), succeed() and trip()"""
    def circuit_breaker(func):
        this_breaker = breaker

        def wrapped(*args, **kwargs):
            this_breaker.guard()
            try:
                result = func(*args, **kwargs)
                this_breaker.succeed()
                return result
            except:
                this_breaker.trip()
                raise
        return wrapped
    return circuit_breaker


class TimeBasedCircuitBreaker:
    """It will be tripped for few seconds if the function fails"""
    def __init__(self, sec):
        self.sec = sec
        self.is_closed = True
        self.last_failure_time = None

    def succeed(self):
        self.is_closed = True

    def trip(self):
        print("tripping...")
        self.is_closed = False
        self.last_failure_time = datetime.now()

    def guard(self):
        now = datetime.now()
        if not self.is_closed and now < self.last_failure_time + timedelta(seconds=self.sec):
            print("still tripped, please retry in",
                  (self.last_failure_time + timedelta(seconds=self.sec) - now).total_seconds(),
                  "seconds")
            raise Exception("This breaker is still tripped")


counter = 1

@circuit_breaker_decorator_factory(TimeBasedCircuitBreaker(3))
def do_something(arg1):
    global counter
    print("== [do_something] is executed", counter, "time" if counter == 1 else "times")
    if counter < 2:
        counter += 1
        raise Exception("Only works after retry")
    return f"Success! argument is [{arg1}]"


if __name__ == "__main__":
    # It will fail at the first try (The circuit breaker becomes "OPEN")
    # Try to execute again next 0.2 seconds on and on
    # But guarded by circuit breaker until the clock time pass 3 sec
    # We can observe that "do_something" only be executed 2 times
    while(1):
        try:
            msg = do_something("Jack")
            print(msg)
            print('counter:', counter)
            break
        except:
            time.sleep(0.2)  # keep triggering do_something intensely
            continue
