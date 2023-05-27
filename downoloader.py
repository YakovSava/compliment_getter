import ctypes

from sys import platform
from os.path import exists

class LoadError(Exception): pass

class Load:

    def __init__(self):
        ends = '.dll' if 'win' in platform else '.so'
        if not exists(f'random{ends}'):
            raise LoadError(f'Load "random{ends}" from path "{path}" failed!')
        self._random_dll = ctypes.CDLL(f'./random{ends}')
        self._c_rand_func = self._random_dll.random
        self._c_rand_func.argtypes = [ctypes.c_int, ctypes.c_int]
        self._c_rand_func.restypes = ctypes.c_int

    def rand(self, from_:int=0, before:int=10) -> int:
        return self._c_rand_func(from_, before)

    def choice(self, array:list=[]):
        assert len(array) != 0, 'Empty list!'
        return array[self.rand(before=len(array))]

    def unsort(self, array:list) -> list:
        new = []
        for _ in array:
            index = self.rand(before=len(array))
            new.append(array[index])
            array.pop(index)
        return new