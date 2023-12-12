pilha = input().split("-")
chuteiras = [ "new balance", "puma", "nike","adidas"]
camisas =  ['endrick','neymar','cr7','messi']
marcas = {
    'endrick': "new balance",
    'neymar': 'puma',
    'cr7': 'nike',
    'messi': 'adidas',
}
camisas_pilha = []
condition = True

for elemento in pilha:
    if elemento in camisas:
        camisas_pilha.append(elemento)
    elif elemento in chuteiras:
        jogador = next(key for key, value in marcas.items() if value == elemento)
        if camisas_pilha and camisas_pilha[-1] == jogador:
           camisas_pilha.pop()
        else:
            condition = False

# A camisas pilha tem que estar vazia se der certo
if condition and not camisas_pilha: 
    print("Correto")
else:
    print("Incorreto")
    