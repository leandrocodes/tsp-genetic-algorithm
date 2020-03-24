import json


def generate(cities):
    return True


def fitness(city):
    return 1


def crossover(a, b):
    return a


def mutate(city):
    return city


def main(iterations):
    return True


if __name__ == "__main__":
    json_file = open("graph.json", encoding="utf8")
    graph = json.load(json_file)

    graph_encoded = {}
    edges_enconded = {}

    for key in graph:
        if (key == "nodes"):
            # print(graph[key])
            count = 0
            for node in graph[key]:
                graph_encoded[node] = count
                count += 1

    for key in graph:
        if (key == "edges"):
            for edge in graph[key]:
                edges_enconded[graph_encoded[edge[0]], graph_encoded[edge[1]]] =  edge[2]


    # print(json.dumps(graph_encoded, indent=4, ensure_ascii=False))
    print(edges_enconded)
