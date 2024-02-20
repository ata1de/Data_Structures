# MST NÃO POLÍTICO 🚩
Os programadores do CIN reinvidicam a recuperação do algoritmo de prim e cabe a você ajudá-los nessa causa tão importante! Para isso você como um experiente programador em grafos irá consertar o código que foi perdido nos servidores do HelpDesk. Você deve usar o código defeituoso abaixo, fazendo as modificações mínimas necessárias para consertá-lo.

Código defeituoso:

import heapq

def prim(grafo):
```
arvore_geradora_minima = []

vertices_visitados = set()

primeiro_vertice = list(grafo.keys())[0]

vertices_visitados.add(primeiro_vertice)

arvore_geradora_minima.append(primeiro_vertice)

arestas_disponiveis = [(peso, primeiro_vertice, vizinho) for vizinho, peso in grafo[primeiro_vertice].items()]

heapq.heapify(arestas_disponiveis)

while arestas_disponiveis:

    pesol, vertice_origeml, vertice_destinol = heapq.heappop(arestas_disponiveis)

    if vertice_destino not in vertices_visitados:

        vertices_visitados.add(vertice_destino)

        arvore_geradora_minima.append((vertice_origem, vertice_destino))

    for vizinho, peso_vizinho in grafo[vertice_destino].items():

        if vizinho in vertices_visitados:

            heapq.heappush(arestas_disponiveis, (peso_vizinho, vertice_destino, vizinho))

return arvore_geradora_minima
```
## Input

Coloque dois objetos setados no seu código:

- grafo_ponderado1 = { 'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2, 'E': 5}, 'C': {'A': 4, 'F': 3, 'G': 7}, 'D': {'B': 2}, 'E': {'B': 5, 'H': 1}, 'F': {'C': 3}, 'G': {'C': 7}, 'H': {'E': 1} }

- grafo_ponderado2 = { 'A': {'B': 4, 'C': 2}, 'B': {'A': 4, 'D': 1, 'E': 7}, 'C': {'A': 2, 'F': 5}, 'D': {'B': 1, 'G': 3}, 'E': {'B': 7, 'H': 2}, 'F': {'C': 5, 'I': 6}, 'G': {'D': 3}, 'H': {'E': 2, 'I': 8}, 'I': {'F': 6, 'H': 8} }

Caso o comando seja **1** utilize o grafo_ponderado1, caso seja **2** utilize o grafo_ponderado2, bem simples!
## Output

A saída do programa consistirá em uma lista de tuplas com duas strings = ( vértice de origem, vértice de destino ), referente aos vértices visitados na ordem do algoritmo e seus vértice anterior.

Exemplo:
```
'A': {'B': 1, 'C': 4},
'B': {'A': 1, 'D': 2, 'E': 5},
'C': {'A': 4, 'F': 3, 'G': 7},
'D': {'B': 2},
'E': {'B': 5, 'H': 1},
'F': {'C': 3},
'G': {'C': 7},
'H': {'E': 1}
```
Onde cada Vértice possui um objeto com suas arestas e o peso, respectivamente.

O output desse grafo é: A, ('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'F'), ('B', 'E'), ('E', 'H'), ('C', 'G')

Nesse caso a ordem de visita foi A -> B -> D -> C -> F -> E -> H -> G. As letras na esquerda das tuplas correspondente ao vértice anterior à aquele visitado.

**PS: O primeiro vértice obviamente não possui nenhum vértice de origem.**