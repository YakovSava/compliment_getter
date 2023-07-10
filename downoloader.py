from rand import random, _overclocking

class Load:

    def __init__(self):
        self._random = random
        _overclocking()

    def rand(self, from_:int=0, before:int=10) -> int:
        return self.random(from_, before)

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