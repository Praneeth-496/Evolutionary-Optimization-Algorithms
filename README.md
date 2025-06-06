# Evolutionary Optimization Algorithms

Implementation and analysis of Genetic Algorithms (GA) and Evolution Strategies (ES) for solving optimization problems F18 (LABS) and F23 (N-Queens/Katsuura). Includes hyperparameter tuning, performance metrics, and visualization of results.

## Table of Contents
- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [Genetic Algorithm (GA)](#genetic-algorithm-ga)
  - [Evolution Strategies (ES)](#evolution-strategies-es)
- [Problems](#problems)
  - [F18 (LABS)](#f18-labs)
  - [F23 (N-Queens/Katsuura)](#f23-n-queenskatsuura)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Experimental Results](#experimental-results)
  - [GA Results](#ga-results)
  - [ES Results](#es-results)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Introduction

This repository contains implementations of two popular evolutionary optimization algorithms: Genetic Algorithms (GA) and Evolution Strategies (ES). These algorithms are applied to solve two benchmark problems: F18 (Low Autocorrelation Binary Sequences) and F23 (N-Queens and Katsuura problems).

Evolutionary algorithms are optimization techniques inspired by biological evolution, using mechanisms such as selection, crossover, and mutation to evolve a population of candidate solutions toward better solutions. They are particularly effective for complex optimization problems where traditional methods may struggle.

## Algorithms

### Genetic Algorithm (GA)

The Genetic Algorithm (GA) implemented in this repository includes the following components:

- **Selection**: Tournament selection with a group size of 3, ensuring competitive selection of parents.
- **Crossover**: Uniform crossover with a configurable crossover rate.
- **Mutation**: Bit-flip mutation, where each bit is flipped with a certain mutation probability.
- **Survivor Selection**: Combined population of parents and offspring is sorted by fitness, and the top individuals are retained for the next generation.

The algorithm follows these steps:
1. **Initialization**: Randomly initialize a population of binary solutions and calculate each individual's fitness.
2. **Selection**: Select individuals for the mating pool based on their fitness.
3. **Crossover**: Combine pairs of selected individuals to create new offspring solutions.
4. **Mutation**: Apply bit-flip mutation to introduce diversity.
5. **Evaluation**: Evaluate the fitness of all individuals in the combined population.
6. **Replacement**: Select the best individuals to form the next generation.
7. **Termination**: Repeat steps 2-6 until the evaluation budget is exhausted.

### Evolution Strategies (ES)

The Evolution Strategy (ES) implemented in this repository is designed to solve the F23 Katsuura problem and includes:

- **Population Initialization**: The initial population of size μ is randomly sampled within the search space.
- **Mutation**: Gaussian mutation with a fixed standard deviation (σ = 0.1) is applied to generate offspring.
- **Selection**: A (μ,λ)-selection strategy is used, where μ = 50 parents produce λ = 100 offspring in each generation.
- **Termination**: The algorithm stops when the total number of function evaluations reaches the predefined budget.

## Problems

### F18 (LABS)

The Low Autocorrelation Binary Sequences (LABS) problem involves finding binary sequences with minimal autocorrelation. This is a challenging combinatorial optimization problem with applications in signal processing and communications.

### F23 (N-Queens/Katsuura)

This repository addresses two variants of the F23 problem:

1. **N-Queens**: The classic problem of placing N queens on an N×N chessboard so that no two queens threaten each other.
2. **Katsuura**: A highly multimodal and non-separable function from the BBOB benchmark suite, posing a significant challenge for optimization algorithms.

## Hyperparameter Tuning

Hyperparameter tuning was conducted by systematically exploring a predefined parameter space:
- Population size: [50, 100, 200]
- Mutation rate: [0.01, 0.05, 0.1]
- Crossover rate: [0.5, 0.7, 0.9]

For each combination of parameters, the algorithms were run for multiple independent trials on both F18 and F23 problems, using a fixed evaluation budget. The best-performing parameters were:
- Population size: 100
- Mutation rate: 0.1
- Crossover rate: 0.9

## Experimental Results

### GA Results

The GA algorithm was evaluated on the F18 LABS and F23 N-Queens problems using:
- **Expected Running Time (ERT)**: Measures the average number of function evaluations required to achieve specific target values.
- **Empirical Cumulative Distribution Function (ECDF)**: Displays the fraction of runs that achieved target values within a given number of evaluations.
- **Average and best fitness values**: For F23, the average best-fitness value was 6.25, with a best fitness of 7. For F18 LABS, the average was 3.82, with a best fitness of 4.33.

### ES Results

The ES algorithm was evaluated on the F23 Katsuura problem using:
- **Expected Running Time (ERT)**: Shows the efficiency in achieving specific target values.
- **Empirical Cumulative Distribution Function (ECDF)**: Demonstrates the algorithm's reliability across multiple runs.
- **Empirical Attainment Function (EAF)**: Visualizes the probability of reaching certain function values within the evaluation budget.

Performance metrics for ES on F23:
- Best Fitness: 7.723
- Average Fitness: 8.161
- Standard Deviation: 0.237

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/evolutionary-optimization-algorithms.git
cd evolutionary-optimization-algorithms

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Genetic Algorithm

```python
# Example code for running the GA on F18
from algorithms.ga import GeneticAlgorithm
from problems.f18 import F18Problem

# Initialize problem
problem = F18Problem(dimension=50)

# Initialize GA with tuned parameters
ga = GeneticAlgorithm(
    population_size=100,
    mutation_rate=0.1,
    crossover_rate=0.9
)

# Run the algorithm
best_solution, best_fitness = ga.run(problem, budget=5000)
print(f"Best fitness: {best_fitness}")
```

### Running the Evolution Strategy

```python
# Example code for running the ES on F23 Katsuura
from algorithms.es import EvolutionStrategy
from problems.f23 import KatsuuraProblem

# Initialize problem
problem = KatsuuraProblem(dimension=10)

# Initialize ES with tuned parameters
es = EvolutionStrategy(
    mu=50,
    lambda_=100,
    sigma=0.1
)

# Run the algorithm
best_solution, best_fitness = es.run(problem, budget=50000)
print(f"Best fitness: {best_fitness}")
```

## Contributors

- Praneeth Dathu (p.dathu@umail.leidenuniv.nl)
- Neeil Nandal (n.s.nandal@umail.leidenuniv.nl)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

