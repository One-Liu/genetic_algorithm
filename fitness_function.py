'''This file is for defining the fitness functions.

1. Evaluates the chromosome.
2. Returns a list with the chromosome and its fitness score.
    I.E. for the triangle classification problem
    Chromosome input: [3,3,3]
    Expected solution input: Equilateral
    Fitness function output: [[3,3,3], 0]
'''
from triangle_classification import Triangle

def classify_triangle(chromosome: list, expected_solution):
    '''Fitness function for triangle classification problem'''
    difference = 0

    a = chromosome[0]
    b = chromosome[1]
    c = chromosome[2]
    triangle = Triangle(a,b,c)
    solution = triangle.get_classification()

    if solution != expected_solution:
        difference = 1

    return [chromosome, difference]
