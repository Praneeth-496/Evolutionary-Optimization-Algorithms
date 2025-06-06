import numpy as np
from ioh import get_problem, logger, ProblemClass

budget = 50000
dimension = 10

np.random.seed(42)

def studentnumber1_studentnumber2_ES(problem):
    # Parameters
    population_size = 50
    offspring_size = 100
    sigma = 0.1 

    # Initialize the population
    population = np.random.uniform(-5, 5, (population_size, dimension))  # Adjust bounds if needed
    fitness = np.array([problem(ind) for ind in population])  # Evaluate initial population

    generation = 0
    print(f"Initial evaluations: {problem.state.evaluations}")

    while problem.state.evaluations < budget:
        # Debugging: Print evaluations at the start of each generation
        print(f"Evaluations: {problem.state.evaluations}, Generation: {generation}")

        # Mutation
        offspring = population[np.random.randint(0, population_size, offspring_size)]  # Select parents
        offspring += np.random.normal(0, sigma, offspring.shape)  # Gaussian mutation

        # Evaluate offspring
        offspring_fitness = np.array([problem(ind) for ind in offspring])

        # Combine population and offspring
        combined_population = np.vstack((population, offspring))
        combined_fitness = np.concatenate((fitness, offspring_fitness))

        # Selection
        top_indices = np.argsort(combined_fitness)[:population_size]
        population = combined_population[top_indices]
        fitness = combined_fitness[top_indices]

        # Print best fitness in the current generation
        generation += 1
        print(f"Generation {generation}, Best Fitness: {min(fitness)}")
    
    # Return the best fitness of the final generation
    return min(fitness)

def create_problem(fid: int):
    # Problem setup
    problem = get_problem(fid, dimension=dimension, instance=1, problem_class=ProblemClass.BBOB)

    # Logger setup
    l = logger.Analyzer(
        root="data",
        folder_name="run",
        algorithm_name="evolution strategy",
        algorithm_info="Practical assignment part2 of the EA course",
    )
    problem.attach_logger(l)
    return problem, l

if __name__ == "__main__":
    F23, _logger = create_problem(23)

    # List to store best fitness from each run
    fitness_results = []

    for run in range(20):
        print(f"Starting Run {run + 1}")
        best_fitness_in_run = studentnumber1_studentnumber2_ES(F23)  # Run the ES
        fitness_results.append(best_fitness_in_run)  # Collect best fitness
        print(f"Run {run + 1} Completed! Best Fitness: {best_fitness_in_run}")
        F23.reset()  # Reset problem after each run

    _logger.close()  # Ensure data is saved

    # Calculate overall statistics
    best_fitness = np.min(fitness_results)
    average_fitness = np.mean(fitness_results)
    std_deviation = np.std(fitness_results)

    print("\nSummary Statistics:")
    print(f"Best Fitness: {best_fitness}")
    print(f"Average Fitness: {average_fitness}")
    print(f"Standard Deviation: {std_deviation}")
