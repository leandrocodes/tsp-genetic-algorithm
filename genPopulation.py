import random

def generate_population(size, x_bound, y_bound):
  lower_x_bound, upper_x_bound = x_bound
  lower_y_bound, upper_y_bound = y_bound

  population = []

  for i in range(rize):
    ind = {
      "x": random.uniform(lower_x_bound, upper_x_bound),
      "y": random.uniform(lower_y_bound, upper_y_bound)
    }
    population.append(ind)
  
  return population
      