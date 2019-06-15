import random

import random_generator
from dna import DNA

TARGET = 'This is the target'
LENGTH_TARGET = len(TARGET)
POPULATION_SIZE = 100
AGENTS = 0
FITNESS_SCORES = 1

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
    agent = DNA(size=LENGTH_TARGET, random_generator=random_generator.RandomLetterGenerator())
    fitness_score = fitness(agent)
    current_population[AGENTS].append(agent)
    current_population[FITNESS_SCORES].append(fitness_score)

best_dna = ''
while best_dna != TARGET:
    last_population = current_population
    current_population = [[], []]
    for i in range(POPULATION_SIZE):
        random_agent, another_random_agent = random.choices(population=last_population[AGENTS], weights=last_population[FITNESS_SCORES], k=2)
        child_agent = random_agent.crossover(another_random_agent).mutated(mutation_rate=0.01)
        child_fitness_score = fitness(child_agent)

        current_population[AGENTS].append(child_agent)
        current_population[FITNESS_SCORES].append(child_fitness_score)
    best_fitness = max(current_population[FITNESS_SCORES])
    best_agent = current_population[AGENTS][current_population[FITNESS_SCORES].index(best_fitness)]
    best_dna = ''.join(best_agent.dna)
    print(best_dna)
