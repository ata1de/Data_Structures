def busca_profundidade(cave, start_room, index):
    stack = [start_room]
    visitados = set()
    # set é um metodo otimizador de pertinência, usei para verificar se a sala ja foi visitada

    while stack:
        current_room = stack.pop(0)

        if current_room == 'Tesouro':
            return True
        
        # Verificando se a sala está dentro da cave
        if current_room <= index and current_room not in visitados:
            visitados.add(current_room)
            if cave[current_room]:  # Verifica se a lista de portas não está vazia
                stack = cave[current_room] + stack

    return False

# Dicionário principal onde contém todas as salas
cave = {}
index = 1

#Tratamento do input
while True:
    inp = input()
    if inp == 'Tesouro':
        cave[index] = ['Tesouro']
        break
    cave[index] = list(map(int, inp.split()))
    index += 1

# Dicion[ario para verificar as salas que ja foram visitadas]
# visitados = {i: False for i in cave.keys()}
treasure = busca_profundidade(cave, 1,  index)

# Output
if treasure:
    print("TESOURO :)")
else:
    print("SEM TESOURO :(")
