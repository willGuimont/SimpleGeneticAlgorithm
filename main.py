import random

import random_generator
from dna import DNA

TARGET = 'This is the target'
LENGTH_TARGET = len(TARGET)
POPULATION_SIZE = 100


def fitness(agent):
    correct = 0
    for i in range(LENGTH_TARGET):
        if TARGET[i] == agent.dna[i]:
            correct += 1
    return correct / LENGTH_TARGET


last_population = []
current_population = [[], []]  # current_population[0] = agent
                               # current_population[1] = fitness

for _ in range(POPULATION_SIZE):
    tmp = DNA(LENGTH_TARGET, random_generator.RandomLetterGenerator())
    fit = fitness(tmp)
    current_population[0].append(tmp)
    current_population[1].append(fit)

best_guess = ''
while best_guess != TARGET:
    last_population = current_population
    current_population = [[], []]
    for i in range(POPULATION_SIZE):
        a, b = random.choices(last_population[0], last_population[1], k=2)
        tmp = a.crossover(b).mutated(0.01)
        fit = fitness(tmp)

        current_population[0].append(tmp)
        current_population[1].append(fit)
    best_guess = current_population[0][current_population[1].index(max(current_population[1]))]
    best_guess = ''.join(best_guess.dna)
    print(best_guess)
