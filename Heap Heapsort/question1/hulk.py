def transformar_em_heap(arr, n, i):
    raiz = arr[0]
    maior = i
    filho_esquerda = 2 * i + 1
    filho_direita = 2 * i + 2

    if filho_esquerda < n and arr[i] < arr[filho_esquerda]:
        maior = filho_esquerda

    if filho_direita < n and arr[maior] < arr[filho_direita]:
        maior = filho_direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        transformar_em_heap(arr, n, maior)

def ordenar_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        transformar_em_heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        transformar_em_heap(arr, i, 0)

def calcular_produto_maximo(arr):
    ordenar_heap(arr)
    return arr[-1] * arr[-2]

# Entrada de exemplo
entrada = input()
numeros = list(map(int, entrada.split(',')))

# Verificar se N >= 2
if len(numeros) < 2:
    print("")
else:
    resultado = calcular_produto_maximo(numeros)
    print("R${}".format(resultado))
