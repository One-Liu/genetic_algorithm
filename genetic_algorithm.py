'''This file is for experimenting with the genetic algorithm

Reference code: 
https://medium.com/@Data_Aficionado_1083/genetic-algorithms-optimizing-success-through-evolutionary-computing-f4e7d452084f
'''
import random

class GeneticAlgorithm:
    '''Class for the Genetic Algorithm'''

    def __init__(self,
                 chromo_len = 3,
                 pop_size = 10,
                 num_generations = 50,
                 selection_type = 'steady-state',
                 selection_rate = 0.5,
                 crossover_type = 'two-point',
                 mutation_type = 'random-resetting',
                 mutation_rate = 0.3
                 ) -> None:
        self._chromo_len = chromo_len
        self._pop_size = pop_size
        self._num_generations = num_generations
        self._selection_type = selection_type
        # Selection rate range = 0 - 1 (0% - 100%)
        self._selection_rate = selection_rate
        self._crossover_type = crossover_type
        self._mutation_type = mutation_type
        # Mutation rate range = 0 - 1 (0% - 100%)
        self._mutation_rate = mutation_rate
        self._current_pop = []

    @property
    def chromo_len(self):
        '''Get chromosome length'''
        return self._chromo_len

    @chromo_len.setter
    def chromo_len(self, chromo_len):
        '''Set chromosome length'''
        self._chromo_len = chromo_len

    @property
    def pop_size(self):
        '''Get population size'''
        return self._pop_size

    @pop_size.setter
    def pop_size(self, pop_size):
        '''Set population size'''
        self._pop_size = pop_size

    @property
    def num_generations(self):
        '''Get number of generations'''
        return self._num_generations

    @num_generations.setter
    def num_generations(self, pop_size):
        '''Set number of generations'''
        self._num_generations = pop_size

    @property
    def selection_rate(self):
        '''Get selection rate'''
        return self._selection_rate

    @selection_rate.setter
    def selection_rate(self, selection_rate):
        '''Set selection rate'''
        self._selection_rate = selection_rate

    @property
    def selection_type(self):
        '''Get selection type'''
        return self._selection_type

    @selection_type.setter
    def selection_type(self, selection_type):
        '''Set selection type'''
        self._selection_type = selection_type

    @property
    def crossover_type(self):
        '''Get crossover type'''
        return self._crossover_type

    @crossover_type.setter
    def crossover_type(self, crossover_type):
        '''Set crossover type'''
        self._crossover_type = crossover_type

    @property
    def mutation_rate(self):
        '''Get mutation rate'''
        return self._mutation_rate

    @mutation_rate.setter
    def mutation_rate(self, mutation_rate):
        '''Set mutation rate'''
        self._mutation_rate = mutation_rate

    @property
    def mutation_type(self):
        '''Get mutation type'''
        return self._mutation_type

    @mutation_type.setter
    def mutation_type(self, mutation_type):
        '''Set mutation type'''
        self._mutation_type = mutation_type

    @property
    def current_pop(self):
        '''Get current population'''
        return self._current_pop

    @current_pop.setter
    def current_pop(self, current_pop):
        '''Set current population'''
        self._current_pop = current_pop

    def create_gen(self):
        '''Creates a gen according with gen type'''
        gen = random.randint(0,100)
        return gen

    def init_pop(self):
        '''Initializes the population'''
        population = []

        for _ in range(self._pop_size):
            chromosome = []
            for _ in range(self._chromo_len):
                chromosome.append(self.create_gen())
            population.append(chromosome)

        return population

    def selection(self, new_pop):
        '''Selects a percentage of the new population for the next generation'''
        selected_new_pop = []

        if self._selection_type == 'random':
            # Randomly selects (selection_rate)% parents
            selected_new_pop = random.sample(new_pop, int(self._selection_rate*self._pop_size))

        elif self._selection_type == 'steady-state':
            # Sorts population by fitness score and then selects the (selection_rate)%
            sorted_new_pop = sorted(new_pop, key=lambda x: x[1])
            selected_new_pop = sorted_new_pop[:int(self._selection_rate*self._pop_size)]

        return selected_new_pop

    def crossover(self, new_pop, current_pop):
        '''Selects random parents according to the selected crossover
        
        For reducing computational costs, we got three similar for loops.
        This way we only need to validate the crossover type once and not 
        n (population size) times.
        '''
        offspring = []

        if self._crossover_type == 'one-point':
            for _ in range(self._pop_size):
                # Gets the chromosome parents from the evaluated lists
                parent1 = random.choice(new_pop)[0]
                parent2 = random.choice(current_pop)[0]

                # Creates children
                point = random.randint(1, self._chromo_len-1)
                child1 = parent1[:point] + parent2[point:]
                child2 = parent2[:point] + parent1[point:]

                # Randomly selects child
                children = [child1, child2]
                offspring.extend([random.choice(children)])

        elif self._crossover_type == 'two-point':
            for _ in range(self._pop_size):
                # Gets the chromosome parents from the evaluated lists
                parent1 = random.choice(new_pop)[0]
                parent2 = random.choice(current_pop)[0]

                # Creates children
                point1 = random.randint(1, (self._chromo_len-2))
                point2 = random.randint(point1+1, (self._chromo_len-1))
                child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
                child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

                # Randomly selects child
                children = [child1, child2]
                offspring.extend([random.choice(children)])

        elif self._crossover_type == 'uniform':
            for _ in range(self._pop_size):
                # Gets the chromosome parents from the evaluated lists
                parent1 = random.choice(new_pop)[0]
                parent2 = random.choice(current_pop)[0]
                parents = [parent1, parent2]

                # Creates children
                child1 = []
                child2 = []
                for chromo in range(self._chromo_len):
                    random.shuffle(parents)
                    child1.append(parents[0][chromo])
                    child2.append(parents[1][chromo])

                # Randomly selects child
                children = [child1, child2]
                offspring.extend([random.choice(children)])

        return offspring

    def mutate(self, offspring):
        '''Mutates the offspring population'''
        mutated_offspring = []

        if self._mutation_type == 'random-resetting':
            for child_chromo in offspring:
                for i in range(self._chromo_len):
                    if self._mutation_rate > random.random():
                        child_chromo[i] = self.create_gen()
                mutated_offspring.append(child_chromo)

        return mutated_offspring

    def replace(self, new_pop, current_pop):
        '''Replaces chromosomes if new gen chromosomes have better fitness score'''
        for _ in range(self._pop_size):
            if current_pop[_][1] > new_pop[_][1]:
                # Replaces chromosome
                current_pop[_][0] = new_pop[_][0]
                # Replaces fitness score
                current_pop[_][1] = new_pop[_][1]

        return current_pop
