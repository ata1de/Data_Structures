class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.anterior = None

class DoublyLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def append(self, element):
        node = Node(element)
        if self.is_empty():
            self.top = node
        else:
            node_atual = self.top
            while node_atual.next:
                node_atual = node_atual.next
            node_atual.next = node
            node.anterior = node_atual

    #Função para adicionar o elemento no inicio da lista
    def push(self, element):
        node = Node(element)
        if not self.is_empty():
            node.next = self.top
            self.top.anterior = node
        self.top = node

    def delete(self, element,index):
        node_atual = self.top
        i = 0
        while node_atual:
            #Caço o elemento pelo seu index, função que eu chamo antes no escopo princpal do código
            if i == index:
                if node_atual.anterior:
                    #O próximo elemento do anterior ao desejado é igual ao proximo do desejado 
                    node_atual.anterior.next = node_atual.next
                else:
                    self.top = node_atual.next

                if node_atual.next:
                    # O elemento anterior ao proximo do desejado é igual ao anterior do desejado
                    node_atual.next.anterior = node_atual.anterior  
            i+=1
            node_atual = node_atual.next
    
    def index(self, element):
        pointer = self.top
        i = 0
        while(pointer):
            if pointer.data == element:
                return i
            i+=1
            pointer = pointer.next
        #SE retornar falso é porque não encontrou o número na lista
        return 'False'

    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + ' '
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
    
    #Criei essa função para tornar meus objetos interáveis, para que no fim eu possa chamar um for em cada um dos elementos
    def __iter__(self):
        pointer = self.top
        while pointer:
            #O yield indica que essa função é um gerado, ou seja, quando interada gerará valores um de cada vez
            yield pointer.data
            pointer = pointer.next


doubly_list = DoublyLinkedList()

while(True):
    action = str(input())
    if action == "Mark fechou o instagram":
        break
    else:
        input_split = action.split(' ')
        #Separo o nome que o Zuck fez a ação para jogá-lo na lista
        name = input_split[-1]
        #Analsando a ação do ZUCK
        ação = input_split[1]
        index_name = doubly_list.index(name)
        #Se a ação foir deixou de seguir, é para tirar o elemento da lista
        if ação != 'deixou':
            #Se o index for igual a False significa que não encontrou na lista, ou seja, não rá haver um duplicado se formos adicionar
            if index_name == 'False':
                doubly_list.push(name)
            else:
                #Ou seja, se o elemento estiver na lista, ele apaga e depois adiciona no topo
                doubly_list.delete(name, index_name)
                doubly_list.push(name)
        # Se a ação for deixar de seguir, deletará o elemento da lista, porém somente se ele tiver na lista
        else:
            if index_name != 'False':
                doubly_list.delete(name, index_name)

for names in doubly_list:
    print(f'{names}')