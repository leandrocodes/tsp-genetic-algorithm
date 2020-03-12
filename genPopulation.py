import random
import math

def generate_population(size, x_bound, y_bound):
  lower_x_bound, upper_x_bound = x_bound
  lower_y_bound, upper_y_bound = y_bound

  population = []

  for i in range(size):
    ind = {
      "x": random.uniform(lower_x_bound, upper_x_bound),
      "y": random.uniform(lower_y_bound, upper_y_bound)
    }
    population.append(ind)
  
  return population

def apply_function(ind):
  x =  ind["x"]
  y = ind["y"]
  return math.sin(math.sqrt(x ** 2 + y ** 2))

generations = 100

population = generate_population(size = 10, x_bound = (-4, 4), y_bound = (-4, 4))
      
i = 1

while True:
  print(f"🧬 GENERATION {i}")

  for ind in population:
    print(ind)

  if i == generations:
    break
  
  i += 1