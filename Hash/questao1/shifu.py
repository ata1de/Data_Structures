class TabelaHash:
    def __init__(self):
        self.agenda = 10
        self.tabela = ['vago'] * self.agenda 

    def calcular_pontos(self, word):
        total = 0
        for letter in word:
            total += ord(letter)
        return total % self.agenda
    
    def inserir(self, lista):
        for palavras in lista:
            indice = self.calcular_pontos(palavras)
            while self.tabela[indice] != 'vago':
                indice+=1
                if indice > 9:
                    indice= -1
                if 'vago' not in self.tabela:
                    break
                    
            self.tabela[indice] = palavras

        return self.tabela




# Seu código para entrada
caracteres = input()
palavras_divididas = []
palavra_acumulada = []
for letra in caracteres:
    if letra in palavra_acumulada:
        palavras_divididas.append(palavra_acumulada)
        palavra_acumulada = [letra]
    else:
        palavra_acumulada.append(letra)

# Adicionar a última palavra
if len(palavra_acumulada) > 0:
    palavras_divididas.append(palavra_acumulada)

# Criação e inserção na tabela hash
tabela_hash = TabelaHash()
nova_tabela = tabela_hash.inserir(palavras_divididas)
print(nova_tabela)




