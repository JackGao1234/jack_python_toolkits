from poc_code import Model_YOU_CANNOT_MODIFY
from utils.bcolor import *


print_header('==Normal Calling==')
a_model = Model_YOU_CANNOT_MODIFY()
a_model.analyze("jack")


def profiling(func):
    def wrapped(*args, **kwargs):
        print_warn("**start timing")
        result = func(*args, **kwargs)
        print_warn("**end timing")
        return result
    return wrapped

print_header('==decorated==')
profiling(a_model.analyze)("jack")


print_header('==Monkey Patching==')
Model_YOU_CANNOT_MODIFY.analyze = profiling(Model_YOU_CANNOT_MODIFY.analyze)  # working on instance method
c_model = Model_YOU_CANNOT_MODIFY()
c_model.analyze("Jack again")
# profiling the instance method without modifying the source code

d_model = Model_YOU_CANNOT_MODIFY()
d_model.analyze("How about another model?")
