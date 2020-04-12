from retrying import retry


class SomeClient:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def refresh(self):
        self.password = 'new password'

    def password_refresh(function):
        def wrapper(self, *args, **kwargs):
            try:
                return function(self, *args, **kwargs)
            except Exception:
                print("---Refreshing... funciton name", function.__name__)
                self.refresh()
                return function(self, *args, **kwargs)

        return wrapper

    @retry(stop_max_attempt_number=2)
    @password_refresh
    def do_something(self, arg1='[arg value 1]'):
        print('1. do_something start...with arg {}'.format(arg1))
        print('2. current password: ', self.password)
        if self.password == 'new password':
            print('3. It works!')
        else:
            print('3. authorization error!!!')
            raise Exception('wrong password')

    @retry(stop_max_attempt_number=3)
    @password_refresh
    def do_another_thing(self, arg1='[arg value 1]'):
        print('1. do_another_thing start...with arg {}'.format(arg1))
        print('2. current password: ', self.password)
        if self.password == 'weird password':  # never passed
            print('3. It works!')
        else:
            print('3. authorization error!!!')
            raise Exception('wrong password')


hi = SomeClient('user id', 'old password')

print('---------------Start do_something-------------------')
hi.do_something()  # works after refresh password
print('---------------Start do_another_thing-------------------')
hi.do_another_thing()  # CANNOT work even password's refreshed
