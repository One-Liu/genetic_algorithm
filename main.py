'''This file is for calling the triangle classification'''
import pandas as pd
from src.models.fitness_evaluation import score_triangle_classification, classify_triangle
from src.models.genetic_algorithm import GeneticAlgorithm

def main():
    '''Main function'''
    ga = GeneticAlgorithm()
    problem = 'triangle-classification'
    expected_solution = 'equilateral'

    if problem == 'triangle-classification':
        get_fitness_score = score_triangle_classification

    # 1) Initialize population
    initial_pop = ga.init_pop()
    generation = 1

    # 2) Calculate fitness score for the current population
    for chromo in range(ga.pop_size):
        evaluated_chromo = get_fitness_score(initial_pop[chromo], expected_solution)
        ga.current_pop.append(evaluated_chromo)

    # 3) Loop until num_generations is reached
    while generation <= ga.num_generations:

        # 3.1) Select best chromosomes from the current population
        selected = ga.selection(ga.current_pop)
        print('Selected:', selected)

        # 3.2) Makes new generation
        crossovered = ga.crossover(selected, ga.current_pop)
        print('Crossovered:', crossovered)

        # 3.3) Diversification
        mutated = ga.mutate(crossovered)
        print('Mutated:', mutated)

        # 3.3.1) Get fitness score for mutated chromosomes
        new_pop = []
        for mutated_chromo in mutated:
            evaluated_chromo = get_fitness_score(mutated_chromo, expected_solution)
            new_pop.append(evaluated_chromo)

        # 3.4) Replace chromosome with new_pop chromosome if new_pop have better fitness score
        ga.current_pop = ga.replace(new_pop, ga.current_pop)

        show_generation(ga, generation)
        generation+=1

def show_generation(ga, generation):
    '''Prints the current gen'''
    print('GENERATION '+ str(generation))

    data = {
        "Fitness score": [],
        "Classification": [],
        "Chromosome": [],
    }

    df = pd.DataFrame(data)

    for element in ga.current_pop:
        chromo = element[0]
        triangle = [chromo[0],chromo[1],chromo[2]]
        df.loc[len(df.index)] = [
            str(element[1]),
            classify_triangle(triangle),
            str(chromo),
        ]

    print(df.to_string())
    print('-'*100)

if  __name__ == '__main__':
    main()
