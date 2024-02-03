def busca_profundidade(cave, start_room, index):
    stack = [start_room]
    visitados = set()
    # set é um metodo otimizador de pertinência, usei para verificar se a sala ja foi visitada

    while stack:
        current_room = stack.pop(0)
        
        # Verificando se a sala está dentro da cave
        if current_room <= index and current_room not in visitados:
            visitados.add(current_room)
            if cave[current_room]:  # Verifica se a lista de portas não está vazia
                stack = cave[current_room] + stack

    return len(visitados)


users, conections = map(int, input().split())
graph = {i:[] for i in range(1, users+1)}

for ramos in range(conections):
    vertice1, vertice2 = map(int, input().split())
    graph[vertice1].append(vertice2)
    graph[vertice2].append(vertice1)

empty = ''
for keys in graph:
    conexão = busca_profundidade(graph, keys, users)
    empty += str(conexão) + " "

print(empty[:-1])
