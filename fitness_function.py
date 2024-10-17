'''This file is for defining the fitness function'''
from triangle_classification import Triangle

class FitnessFunction:
    '''Class to get the fitness score according with the problem'''
    def __init__(self, problem: str, expected_solution: str) -> None:
        self.problem = problem
        self.expected_solution = expected_solution

    def get_fitness_score(self, chromosome: list):
        '''Evaluates the chromosome
        
        Returns a list with the chromosome and its fitness score
        '''
        difference = 0

        if self.problem == 'triangle-classification':
            a = chromosome[0]
            b = chromosome[1]
            c = chromosome[2]
            triangle = Triangle(a,b,c)
            solution = triangle.get_classification()

            if solution != self.expected_solution:
                difference = 1

        return [chromosome, difference]
