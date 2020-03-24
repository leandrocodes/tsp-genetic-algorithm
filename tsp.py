import json
import random

def generate(cities, individues):
    cities_list = list(cities.values())
    cities_list.pop(0)
    # print(cities_list)
    # print(random.sample(cities_list, len(cities_list)))
    population = []
    
    for ind in range(individues):
        population.append(random.sample(cities_list, len(cities_list)))
    
    # print(population)
    return population

def fitness(edges, population):
    for crom in population:
        temp = [0] + crom + [0]
        for i in range(len(temp)-1):
            print(temp[i], temp[i+1])

def crossover(a, b):
    return a


def mutate(city):
    return city


def main(iterations):
    return True


if __name__ == "__main__":
    json_file = open("graph.json", encoding="utf8")
    graph = json.load(json_file)

    nodes_encoded = {}
    edges_enconded = {}

    for key in graph:
        if (key == "nodes"):
            # print(graph[key])
            count = 0
            for node in graph[key]:
                nodes_encoded[node] = count
                count += 1

    for key in graph:
        if (key == "edges"):
            for edge in graph[key]:
                edges_enconded[nodes_encoded[edge[0]], nodes_encoded[edge[1]]] =  edge[2]


    # print(json.dumps(nodes_encoded, indent=4, ensure_ascii=False))
    # print(edges_enconded)

    population = generate(nodes_encoded, 10)
    fitness(edges_enconded, population)