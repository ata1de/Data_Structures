class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class HeapTree:
    def __init__(self):
        self.root = None
    
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

    def toTop(self):
        pass


# Exemplo de uso
heap_tree = HeapTree()
lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heap_tree.insert(lista_exemplo)
print('oi')
