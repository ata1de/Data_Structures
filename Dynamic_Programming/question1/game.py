def max_soma(lista):
    if not lista:
        return 0

    n = len(lista)
    dp = [0] * (n + 1)

    # criação do container de soma e inicio do caso base
    dp[0] = 0
    dp[1] = lista[0]

    # Preenchimento da tabela 
    for i in range(2, n + 1):
        # aqui ocorre a condição de somar somente com os não adjacentes,
        # pois tem a verificação se a soma anterior é maior que a soma atual
        dp[i] = max(dp[i - 1], dp[i - 2] + lista[i - 1])

    # retorna o ultimo elemento pois ele sempre será o maior
    return dp[n]

arquibancadas = int(input())
torcedores = list(map(int, input().split()))
resultado = max_soma(torcedores)
print(f'{resultado} torcedores podem ser fotografados.')
