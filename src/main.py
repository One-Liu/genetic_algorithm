"""This file is for executing the GA and printing its results"""
from pandas import DataFrame
from src.models.ga.genetic_algorithm import GeneticAlgorithm

def main():
    """Main function to execute the GA"""
    ga = GeneticAlgorithm()
    ga.init_pop()
    conf, exec_data = ga.execute()
    df_conf = DataFrame(conf)
    df_exec_data = DataFrame(exec_data)
    print(df_conf.to_string())
    print(df_exec_data.to_string())

if  __name__ == '__main__':
    main()
