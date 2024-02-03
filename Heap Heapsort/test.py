class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class HeapTree:
    def __init__(self):
        self.root = None
        self.tree = []
    
    def insert(self, list):
        self.root = Node(list[0])
        # FORMA DE NÃO CRIAR NOVOS NOS E PEGAR OS EXISTENTES
        pilha = [self.root]

        for i in range(1, len(list)):
            elemento = list[i]
            node = Node(elemento)

            # AO PROCURARMOS PELA CABEÇA DA PILHA, ANALISAMOS SE ELE TEM A ESQUERDA OU A DIREITA
            head = pilha[0]
            if not head.left:
                # VERIFICANDO SE A CONDIÇÃO DE NÃO PODER O NO TER FILHOS MAIORES ESTÁ CONDIZENTE
                if node.data > head.data:
                    # VARIVALE PARA ARMZENAR O VALOR DO NO
                    container = head.data
                    head.data = node.data
                    node.data = container
                head.left = node
            # QUANDO TIVER ADICIONARMOS A DIREITA, APAGAMOS ELE DA PILHA E ANALISAMOS O OUTRO NOS
            else:
                # VERIFICANDO SE A CONDIÇÃO DE NÃO PODER O NO TER FILHOS MAIORES ESTÁ CONDIZENTE
                if node.data > head.data:
                    # VARIVALE PARA ARMZENAR O VALOR DO NO
                    container = head.data
                    head.data = node.data
                    node.data = container

                head.right = node
                pilha.pop(0)

            # POR FIM, LIGAMOS O FILHO AO PAI
            node.parent = head
            pilha.append(node)

        self.Max(list)

    def Max(self,list):
        pass
        

    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.tree.append(node.data)
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)
        else:
           self.tree.append(node.data)



# Exemplo de uso
heap_tree = HeapTree()
lista_exemplo = input().split()
lista_exemplo2 = list(map(int, lista_exemplo))
heap_tree.insert(lista_exemplo2)
heap_tree.preorder_traversal()
print(heap_tree.tree)
