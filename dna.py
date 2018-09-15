import random


class DNA:
    def __init__(self, size: int, random_generator):
        self.random_generator = random_generator
        self.dna = [random_generator.gen() for _ in range(size)]

    def crossover(self, other, self_probability=0.5):
        self_size = len(self.dna)
        assert self_size == len(other.dna)
        new = DNA(self_size, self.random_generator)
        for i, dnas in enumerate(zip(self.dna, other.dna)):
            a, b = dnas
            if random.uniform(0, 1) < self_probability:
                new.dna[i] = self.dna[i]
            else:
                new.dna[i] = other.dna[i]
        return new

    def mutated(self, mutation_rate: float):
        self_size = len(self.dna)
        new = DNA(self_size, self.random_generator)
        new.dna = self.dna.copy()
        for i in range(self_size):
            if random.uniform(0, 1) < mutation_rate:
                new.dna[i] = self.random_generator.gen()
        return new
