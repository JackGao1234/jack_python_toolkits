import abc

from utils.bcolor import print_warn


class Fantasy(abc.ABC):
    @abc.abstractmethod
    def rush(self):
        return NotImplemented

    @classmethod
    @abc.abstractmethod
    def glance(cls):
        return NotImplemented

    @staticmethod
    @abc.abstractmethod
    def touch():
        return NotImplemented

    @property
    @abc.abstractmethod
    def dance(self):
        return NotImplemented


class DreamsComeTrue(Fantasy):
    def __init__(self):
        self._dance = "dancing"

    def rush(self):
        print("rushed")

    @classmethod
    def glance(cls):
        print("seen")

    @staticmethod
    def touch():
        print("touched")

    @property
    def dance(self):
        try:
            return self._dance
        except AttributeError:
            raise ValueError('No feathers')

    @dance.setter
    def dance(self, new):
        print_warn("before setting [dance]:", self._dance)
        self._dance = new
        print_warn("after setting [dance]:", self._dance)


a = DreamsComeTrue()
a.rush()
a.__class__.glance()
a.touch()
print(a.dance)
a.dance = "1, 2, 1, 2, 3, 4"
print(a.dance)
