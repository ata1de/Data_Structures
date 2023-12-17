# 👕 BORA SOLTE MINHA CAMISA
Recentemente um fenômeno anormal vem acontecendo nas estações por todo o Brasil, aparentemente camisas estão sendo puxadas e o dono da camisa não consegue descobrir quem é o culpado por tal importunação. Sabendo disso, professor Sergio de algoritmos teve uma ideia, chamar todos que estão na estação e entregar camisas numeradas, as quais devem ser ordenadas por meio de uma árvore binária, pois a pessoa vestindo a camisa com o número mais à esquerda da árvore será a responsável por puxar a camisa da raiz da árvore, isso graças a um método de pesquisa desenvolvido pelo professor Sérgio, sabendo que a raiz é o primeiro número lido e os seguites serão adicionados conforme as especificações da árvore, onde um item menor é adicionado à esquerda e um maior à direita. Mas para não te deixar desamparado um trecho de código foi disponibilizado para te ajudar:

## Code
```
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
        ***

        ***
```

### Inputs
Será disponibilizado um sequencia de números, que simbolizam os números da camisa de cada um
```
2 1 3 4 5
```

### Outputs
```
1 puxou a camisa de 2
```