class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.next = None
        self.right = None
        self.left = None
        self.children = 0

    
class Tree:
    def __init__(self, node=None):
        if node is None:
            self.root = None
        else:
            self.root = Node(node)

    def insert(self,list):
        if not self.root:
            self.root = list[0]
        for i in range(len(list)):
                elemento = list[i]
                node = Node(elemento)

                # ADICIONANDO O ELEMENTO A ESQUERDA
                index_left = ((2*i) + 1)
                if index_left <= len(list)-1:
                    elemento_esquerda = list[(2*i) + 1]
                    node.left = Node(elemento_esquerda)

                # Adicionando o elemento a direita
                index_right = ((2*i) + 2)
                if index_right <= len(list)-1:
                    elemento_direita = list[(2*i) + 2]
                    node.right = Node(elemento_direita)

                # Se o elemento for a raiz não tem parent
                if i ==0:
                    node.parent = None
                else:
                    elemento_pai = list[int((i - 1)/2)]
                    node.parent = Node(elemento_pai)
         


tree = Tree()
lista_exemplo = input().split()
lista_exemplo2 = list(map(int, lista_exemplo))
tree.insert(lista_exemplo2)
print('oi')

