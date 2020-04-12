"""
    Enum is to manage something will not change, e.g. magic number/string, constants
        - Easier to tell other people what do the magic numbers/strings mean
        - Avoid changing many places of code when a functionality changed
        - Reduce the probability of typos
        - ...

    Official Doc: https://docs.python.org/3.6/library/enum.html
"""
from enum import Enum


class Env(Enum):
    """Align running env for whole application"""
    PROD = 'Production Environment'
    TEST = 'Test Environment'
    DEV = 'Development Environment'


print('-------Customized Environments-------')
print(Env.PROD)
env = Env.DEV
if env == Env.DEV:
    print("it's in DEV environment.")


class RestfulApiUrl(Enum):
    RESTFUL_API_PROD_URL = 'http://some.api.prod/'
    RESTFUL_API_TEST_URL = 'http://some.api.test/'


print('-------RESTful API urls-------')
print(RestfulApiUrl.RESTFUL_API_PROD_URL.name)
print(RestfulApiUrl.RESTFUL_API_TEST_URL.value)

print('--------constant value in ENUM-------')


class MyEndpoint(Enum):
    ENDPOINT_ROOT = 'endpoint_root/'
    A = ENDPOINT_ROOT + 'A'
    B = ENDPOINT_ROOT + 'B'
    C = ENDPOINT_ROOT + 'C'
    D = ENDPOINT_ROOT + 'D'
    E = ENDPOINT_ROOT + 'E'
    F = ENDPOINT_ROOT + 'F'


for endpoint in MyEndpoint:
    print(endpoint.name, ': ', endpoint.value)

print('------------nested ENUM------------------')


class NestedEndpoint(Enum):
    """
        lowercase ENUMs have something inside (nested)
        uppercase ENUMs are the API endpoints
    """

    class _root1(Enum):
        ROOT_ENDPOINT = 'root1/'
        A = ROOT_ENDPOINT + 'A'
        B = ROOT_ENDPOINT + 'B'
        C = ROOT_ENDPOINT + 'C'

    class _root2(Enum):
        ROOT_ENDPOINT = 'root2/'
        EMPTY = ROOT_ENDPOINT + ''
        D = ROOT_ENDPOINT + 'D'
        E = ROOT_ENDPOINT + 'E'

    root1 = _root1
    root2 = _root2


print(NestedEndpoint.root1.value.A.value)
print(NestedEndpoint.root2.value.E.value)

print('------------Sometimes flat is better than nested--------------------')


class EndpointFlatten(Enum):
    """
        double underscores mean slashes
    """
    root1 = 'root1/'
    root1__A = root1 + 'A'
    root1__B = root1 + 'B'
    root1__C = root1 + 'C'

    root2 = 'root2/'
    root2__D = root2 + 'D'
    root2__E = root2 + 'E'
    root2__F = root2 + 'F'


print(EndpointFlatten.root1.value)
print(EndpointFlatten.root2__E.value)

print('------------CAUTION: VERY, VERY advanced design for Enum------------------')


class EmployeeJobTitle(Enum):
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    @property
    def ANNUAL_BASE_SALARY(self):
        ANNUAL_MONTH_DEFAULT = 14  # 14 months PER year
        return self.salary * ANNUAL_MONTH_DEFAULT


# Don't ask. It's just sample data
class Manager(EmployeeJobTitle):
    M1 = ('M1', 2_000)
    M2 = ('M2', 4_000)
    M3 = ('M3', 6_000)
    M4 = ('M4', 8_000)


class Engineer(EmployeeJobTitle):
    E1 = ('E1', 10_000)
    E2 = ('E2', 20_000)
    E3 = ('E3', 30_000)
    E4 = ('E4', 40_000)
    E5 = ('E5', 50_000)
    E6 = ('E6', 60_000)


print('Annual base salary for M1 is:', Manager.M1.ANNUAL_BASE_SALARY)
print('Annual base salary for E3 is:', Engineer.E3.ANNUAL_BASE_SALARY)
