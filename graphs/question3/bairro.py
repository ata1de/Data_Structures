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

    return visitados

bairro, _ = input().split()
bairros = {}
numero_bairro = []

for b in range(int(bairro)):
    conexoes = input().split(": ")
    nome_e_numero_bairro = conexoes.pop(0)
    ligações= conexoes[0].split(', ')
    nome, numero = nome_e_numero_bairro.split()
    ligações_final = [int(x) for x in ligações]
    bairros[int(numero)] = ligações_final
    numero_bairro.append(int(numero))

visitados = busca_profundidade(bairros, 0, int(bairro))

for num in numero_bairro[1:]:
    if num in visitados:
        print(f'Bairro {num}: Pode!')
    else:
        print(f'Bairro {num}: Não pode!')

