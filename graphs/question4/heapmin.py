import heapq

def encontrar_arvore_geradora_minima(grafo):
    arvore_geradora_minima = []
    vertices_visitados = set()
    primeiro_vertice = list(grafo.keys())[0]
    vertices_visitados.add(primeiro_vertice)
    arestas_disponiveis = [(peso, primeiro_vertice, vizinho) for vizinho, peso in grafo[primeiro_vertice].items()]
    heapq.heapify(arestas_disponiveis)

    while arestas_disponiveis:
        peso, vertice_origem, vertice_destino = heapq.heappop(arestas_disponiveis)
        if vertice_destino not in vertices_visitados:
            vertices_visitados.add(vertice_destino)
            arvore_geradora_minima.append((vertice_origem, vertice_destino))
            for vizinho, peso_vizinho in grafo[vertice_destino].items():
                if vizinho not in vertices_visitados:
                    heapq.heappush(arestas_disponiveis, (peso_vizinho, vertice_destino, vizinho))
    return arvore_geradora_minima

# Grafos fornecidos
grafo_ponderado1 = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3, 'G': 7},
    'D': {'B': 2},
    'E': {'B': 5, 'H': 1},
    'F': {'C': 3},
    'G': {'C': 7},
    'H': {'E': 1}
}

grafo_ponderado2 = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 1, 'E': 7},
    'C': {'A': 2, 'F': 5},
    'D': {'B': 1, 'G': 3},
    'E': {'B': 7, 'H': 2},
    'F': {'C': 5, 'I': 6},
    'G': {'D': 3},
    'H': {'E': 2, 'I': 8},
    'I': {'F': 6, 'H': 8}
}

# Input
opcao = input()
grafo = grafo_ponderado1 if opcao == '1' else grafo_ponderado2

# Encontrar a árvore geradora mínima
arvore_minima = encontrar_arvore_geradora_minima(grafo)

# Output
output = "A"
for aresta in arvore_minima:
    output += ", " + str(aresta)
print(output)
