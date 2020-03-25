import json
import random
from itertools import combinations

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

def getFitness(edges, population):
    fitness = []
    for crom in population:
        fit = 0
        temp = [0] + crom + [0]
        # print(temp)
        for i in range(len(temp)-1):
            edge = (temp[i], temp[i+1])
            if (edge not in edges.keys()):
                edge = (temp[i+1], temp[i])
            
            fit += edges[edge]
        fitness.append((crom, 1/fit))
    
    # print(fitness)
    return fitness

def selection(fitPopulation):
    selPopulation = []
    sum_fit = sum(list(map(lambda fit: fit[1], fitPopulation)))
    p = [ pop[1]/sum_fit for pop in fitPopulation ]
    
    while len(selPopulation) < len(fitPopulation):
        soma = 0
        pointer = random.random()

        for i in range(len(p)):
            soma += p[i]
            if (pointer < soma):
                selPopulation.append(fitPopulation[i][0])
                break
    
    print(selPopulation)
    return selPopulation

def crossover(prob, selPopulation):
    cross_pop = []
    count = 0
    while len(cross_pop) != len(selPopulation):
        for indi in selPopulation:
            for comb in combinations(selPopulation, 2):
                if(random.random() <= prob):
                    if (count == 2): break
                    cut1 = random.randint(1, 4)
                    cut2 = random.randint(1, 4)
                    ind1, ind2 = comb
                    temp1 = ind1[0][:cut1]
                    temp2 = ind2[0][cut2:]
                    
                    for gene in temp2:
                        if(gene not in temp1):
                            temp1.append(gene) 
                    
                    while len(temp1) < 5:
                        for gene in ind2[0]:
                            if(gene not in temp1):
                                temp1.append(gene) 

                    for gene in temp1:
                        if(gene not in temp2):
                            temp2.append(gene) 
                    
                    while len(temp2) < 5:
                        for gene in ind1[0]:
                            if(gene not in temp2):
                                temp2.append(gene) 
                            
                    # print(ind1[0], ind2[0])
                    count += 1
                    # print(temp1, temp2)
                    cross_pop.append(temp1)
                    cross_pop.append(temp2)
        
        cross_pop.append(indi)
    
    return cross_pop
        


def mutate(city):
    return city


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
                edges_enconded[(nodes_encoded[edge[0]],
                                nodes_encoded[edge[1]])] = edge[2]

    # print(json.dumps(nodes_encoded, indent=4, ensure_ascii=False))
    # print(edges_enconded)

    population = generate(nodes_encoded, 10)
    fitPopulation = getFitness(edges_enconded, population)
    selPopulation = selection(fitPopulation)
    cross = crossover(0.7, fitPopulation)