import random
from Utils import Chromosome, Food

class GAEngine:
    
    def __init__(self):
        self.population = []
        self.food = []
        self.generations = 0

    def make_initial_population(self, population_size):   
        for i in range(population_size):
            self.population.append(Chromosome(random.randint(0, 790), random.randint(0, 590)))

    def add_food(self, no_of_food):  
        self.food = []   
        for i in range(no_of_food):
            self.food.append(Food(random.randint(0, 790), random.randint(0, 590)))

    # selection code goes here...
    def do_crossover(self, no_of_offspring):
        offspring = []
        for _ in range(no_of_offspring):
            parent1, parent2 = [self.population[0], self.population[1]]
        
            # Single-point crossover logic
            x = random.choice([parent1.x_pos, parent2.x_pos])
            y = random.choice([parent1.y_pos, parent2.y_pos])
        
            child = Chromosome(x, y)  # Create a new Chromosome (offspring)
            child.mutate()
            offspring.append(child)
        
        self.population = self.population[:-no_of_offspring] + offspring
    
        # self.population.extend(offspring)  # Add offspring to the population

    # fitness calculation goes here...
    def assign_fitness(self):
        for i in self.population:
            distance = i.get_distance_to(self.food[0])
            if distance == 0:
                fitness_score = float('inf')
            else:
                fitness_score = 1/distance
            i.fitness = fitness_score

    def sort_by_fitness(self):
        self.population.sort(key=lambda i: i.fitness, reverse=True)

    def get_population(self):
        return self.population

    def get_foods(self):
        return self.food