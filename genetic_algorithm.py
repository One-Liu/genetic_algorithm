'''This file is for experimenting with the genetic algorithm

Reference code: 
https://medium.com/@Data_Aficionado_1083/genetic-algorithms-optimizing-success-through-evolutionary-computing-f4e7d452084f
'''
import random
import pandas as pd
from fitness_function import FitnessFunction
from triangle_classification import Triangle

class GeneticAlgorithm:
    '''Class for the Genetic Algorithm'''

    def __init__(self,
                 chromo_len = 3,
                 pop_size = 10,
                 num_generations = 50,
                 selection_type = 'steady-state',
                 selection_rate = 0.5,
                 crossover_type = 'one-point',
                 mutation_type = '',
                 mutation_rate = 0.3,
                 problem = 'triangle-classification',
                 expected_solution = 'isosceles',
                 ) -> None:
        self.chromo_len = chromo_len
        self.pop_size = pop_size
        self.num_generations = num_generations

        # Selection rate range = 0 - 1 (0% - 100%)
        self.selection_rate = selection_rate
        self.selection_type = selection_type

        self.crossover_type = crossover_type

        # Mutation rate range = 0 - 1 (0% - 100%)
        self.mutation_rate = mutation_rate
        #TODO
        self.mutation_type = mutation_type

        self.fitness_function = FitnessFunction(problem, expected_solution)
        self.current_pop = []

    def init_pop(self):
        '''Initializes the population'''
        population = []

        for i in range(self.pop_size):
            chromosome = []
            for j in range(self.chromo_len):
                #TODO: Generate gens according with type (bit, real number, permutation)
                # GEN CREATION
                chromosome.append(random.randint(0,100))
            population.append(chromosome)

        return population

    def selection(self, new_pop):
        '''Selects a percentage of the new population for the next generation'''
        selected_new_pop = []

        if self.selection_type == 'random':
            # Randomly selects (selection_rate)% parents
            selected_new_pop = random.sample(new_pop, int(self.selection_rate*self.pop_size))

        elif self.selection_type == 'steady-state':
            # Sorts population by fitness score and then selects the (selection_rate)%
            sorted_new_pop = sorted(new_pop, key=lambda x: x[1])
            selected_new_pop = sorted_new_pop[:int(self.selection_rate*self.pop_size)]

        return selected_new_pop

    def crossover(self, new_pop, current_pop):
        '''Selects random parents according to the selected crossover'''
        offspring = []

        if self.crossover_type == 'one-point':
            for _ in range(self.pop_size):
                # Gets the chromosome parents from the evaluated lists
                parent1 = random.choice(new_pop)[0]
                parent2 = random.choice(current_pop)[0]

                # Creates children
                crossover_point = random.randint(1, self.chromo_len-1)
                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]

                # Randomly selects child
                children = [child1, child2]
                offspring.extend([random.choice(children)])

        elif self.crossover_type == 'two-point':
            #TODO
            pass
        elif self.crossover_type == 'uniform':
            #TODO
            pass

        return offspring

    def mutate(self, offspring):
        '''Mutates the offspring population'''
        mutated_offspring = []

        for child_chromo in offspring:
            for i in range(self.chromo_len):
                #TODO: Check if mutation rate is applied correctly
                if self.mutation_rate > random.random():
                    # GEN CREATION
                    child_chromo[i] = random.randint(0,100)
            mutated_offspring.append(child_chromo)

        return mutated_offspring

    def replace(self, new_pop, current_pop):
        '''Replaces chromosomes if new gen chromosomes have better fitness score'''
        for _ in range(self.pop_size):
            if current_pop[_][1] > new_pop[_][1]:
                # Replaces chromosome
                current_pop[_][0] = new_pop[_][0]
                # Replaces fitness score
                current_pop[_][1] = new_pop[_][1]

        return current_pop

    def execute(self):
        '''Executes the algorithm'''
        # 1) Initialize population
        initial_pop = self.init_pop()
        generation = 1

        # 2) Calculate fitness score for the current population
        for chromosome in range(self.pop_size):
            evaluated_chromo = self.fitness_function.get_fitness_score(initial_pop[chromosome])
            self.current_pop.append(evaluated_chromo)

        # 3) Loop until num_generations is reached
        while generation <= self.num_generations:

            # 3.1) Select best chromosomes from the current population
            selected = self.selection(self.current_pop)
            print('Selected:', selected)

            # 3.2) Makes new generation
            crossovered = self.crossover(selected, self.current_pop)
            print('Crossovered:', crossovered)

            # 3.3) Diversification
            mutated = self.mutate(crossovered)
            print('Mutated:', mutated)

            # 3.3.1) Get fitness score for mutated chromosomes
            new_pop = []
            for mutated_chromo in mutated:
                evaluated_chromo = self.fitness_function.get_fitness_score(mutated_chromo)
                new_pop.append(evaluated_chromo)

            # 3.4) Replace chromosome with new_pop chromosome if new_pop have better fitness score
            self.current_pop = self.replace(new_pop, self.current_pop)

            self.__show_generation(generation)
            generation+=1

    def __show_generation(self, generation):
        '''Prints the current gen'''
        print('GENERATION '+ str(generation))

        data = {
            "Fitness score": [],
            "Classification": [],
            "Chromosome": [],
        }

        df = pd.DataFrame(data)

        for element in self.current_pop:
            chromo = element[0]
            triangle = Triangle(chromo[0],chromo[1],chromo[2])
            df.loc[len(df.index)] = [
                str(element[1]),
                triangle.get_classification(),
                str(chromo),
            ]

        print(df.to_string())
        print('-'*100)
