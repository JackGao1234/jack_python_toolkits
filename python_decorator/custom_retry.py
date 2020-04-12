from utils.bcolor import print_warn


def my_retry(func):
    def wrap(*args, **kwargs):
        for i in range(1, 6):
            try:
                print_warn("attemps:", i)
                result = func(*args, **kwargs)
                break
            except:
                if i != 5:
                    continue
                else:
                    raise
        return result

    return wrap


@my_retry
def greet(user):
    print("must be printed")
    # raise ValueError("no no")  # (un)comment to practice
    print(f"greet: {greet.__name__}")
    print(f"Hello {user}")


greet("Jack")
