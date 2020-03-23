cities = [
    [0, 325, 420, 230, 143, 189],
    [325, 0, 335, 270, 285, 474],
    [420, 335, 0, 588, 563, 609],
    [230, 270, 588, 0, 373, 413],
    [189, 474, 609, 413, 213, 0]
]

for city in cities:
    print(city)

def fitness(city):
    return 1

def crossover(a, b):
    return a

def mutate(city):
    return city

def main(iterations):
    return True