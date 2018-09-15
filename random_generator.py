import abc
import string
import random


class RandomGenerator(abc.ABC):
    @abc.abstractmethod
    def gen(self):
        ...


class UniformFloatGenerator(RandomGenerator):
    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def gen(self):
        return random.uniform(self.min, self.max)


class RandomLetterGenerator(RandomGenerator):
    def __init__(self):
        self.alphabet = string.ascii_letters + ' '

    def gen(self):
        return random.choice(self.alphabet)


class RandomIntGenerator(RandomGenerator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def gen(self):
        return random.randint(self.min_value, self.max_value)


class BinaryGenerator(RandomIntGenerator):
    def __init__(self):
        super().__init__(0, 1)
