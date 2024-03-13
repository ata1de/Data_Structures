def dp(index, planetas, memo, n):
    # aqui ocorre uma recursão, mas com programação dinamica
    if index in memo:
        return memo[index]

    paths = [[planetas[index]]]
    for i in range(index + 1, n):
        for path in dp(i, planetas, memo, n):
            # ele adiciona os planetas + o proprio planeta do index
            paths.append([planetas[index]] + path)

    # atualiza o memo para o funcionamento da programação dinamica
    memo[index] = paths
    return paths

def visitacoes_possiveis(planetas):
    # retorna lista vazia pois não tem planetas para visitar
    if not planetas or planetas[0] == ' ':
        return [[]]

    n = len(planetas)
    # dicionário onde ficará armazenados os dados para ser usado na busca dos planetas
    memo = {}

    all_paths = [[]]
    for i in range(n):
        all_paths.extend(dp(i, planetas, memo, n))

    return all_paths

# INPUT
galaxys = input().split(', ')
galaxys.sort()
# OUTPUTS
outputs = visitacoes_possiveis(galaxys)
print(f'O número de subsets de visitação é {len(outputs)}')
print(f'São eles: {outputs}')
