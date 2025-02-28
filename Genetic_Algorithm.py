import random

POPULATION_SIZE = 10
GENE_LENGTH = 8
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7
GENERATIONS = 50

def fitness_function(individual):

    x = int(''.join(map(str, individual)), 2)
    return x ** 2

def create_individual():
    return [random.randint(0, 1) for _ in range(GENE_LENGTH)]

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]  # Flip the bit
    return individual

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, GENE_LENGTH - 1)
        return (parent1[:point] + parent2[point:], parent2[:point] + parent1[point:])
    return parent1, parent2

def select_individual(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            return individual

population = [create_individual() for _ in range(POPULATION_SIZE)]

for generation in range(GENERATIONS):
    fitnesses = [fitness_function(individual) for individual in population]

    best_fitness = max(fitnesses)
    print(f"Generation {generation}: Best Fitness = {best_fitness}")

    new_population = []
    while len(new_population) < POPULATION_SIZE:
        parent1 = select_individual(population, fitnesses)
        parent2 = select_individual(population, fitnesses)

        offspring1, offspring2 = crossover(parent1, parent2)

        offspring1 = mutate(offspring1)
        offspring2 = mutate(offspring2)

        new_population.extend([offspring1, offspring2])

    population = new_population[:POPULATION_SIZE]

best_individual = max(population, key=fitness_function)
best_x = int(''.join(map(str, best_individual)), 2)
print(f"Best individual: {best_individual}, x = {best_x}, Fitness = {best_x ** 2}")