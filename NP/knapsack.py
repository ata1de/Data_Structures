def knapsack_partition(S):
    total = sum(S)
    if total % 2 != 0:
        # Se a soma total não for par, não é possível encontrar uma partição.
        return None

    capacity = total // 2
    n = len(S)

    # Inicializando a tabela de programação dinâmica.
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Preenchendo a tabela de programação dinâmica.
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if S[i - 1] <= j:
                DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - S[i - 1]] + S[i - 1])
            else:
                DP[i][j] = DP[i - 1][j]

    # Verificando se encontramos uma solução.
    if DP[n][capacity] == capacity:
        # Recuperando os itens selecionados.
        selected_items = []
        i, j = n, capacity
        while i > 0 and j > 0:
            if DP[i][j] != DP[i - 1][j]:
                selected_items.append(S[i - 1])
                j -= S[i - 1]
            i -= 1
        return selected_items
    else:
        return None

# Exemplo de uso:
S = [1, 2, 3, 4, 5, 6]
solution = knapsack_partition(S)
if solution is not None:
    print("Solução encontrada:", solution)
else:
    print("Não foi possível encontrar uma solução.")
