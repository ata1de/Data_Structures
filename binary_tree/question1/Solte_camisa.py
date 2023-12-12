class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.direita = None
        self.esquerda = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        item = Node(valor)

        if self.raiz == None:
            self.raiz = item
        
        else:
            adicionado = False
            itemAtual = self.raiz
            while not adicionado:
                if itemAtual.valor < item.valor:
                    if itemAtual.direita == None:
                        itemAtual.direita = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.direita
                else:
                    if itemAtual.esquerda == None:
                        itemAtual.esquerda = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.esquerda
    
    def buscaCulpado(self):
      if self.raiz is None:
        return None
        
      node = self.raiz
      while node.esquerda:
        node = node.esquerda
      return node.valor
      
    def displayRoot(self):
      return self.raiz.valor
      

numeros_camisas = [int(x) for x in input().split()]

arvore = Arvore()
for numero in numeros_camisas:
    arvore.inserir(numero)

culpado = arvore.buscaCulpado()
raiz = arvore.displayRoot()
print(f"{culpado} puxou a camisa de {raiz}")
      
      
        