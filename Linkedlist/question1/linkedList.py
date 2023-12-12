class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def append(self, element):
        if self.start != None:
            pointer = self.start
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.start = Node(element)
        self.size+=1

    def remove(self,element):
        found = False #Variávelç ṕara indicar se achou o número ou não
        if self.start == None:
            print(f"Node {element} não existe")
            found = True
        #SE a cabeça da lista for o alvo, a cabeça vira o próximo elemento da lista
        elif self.start.data == element:
            self.start = self.start.next
            print(f"Node {element} foi removido")
            self.size-=1
        else:
            antecessor = self.start
            pointer = self.start.next
            while(pointer):
                if pointer.data == element:
                    antecessor.next = pointer.next
                    pointer.next = None
                    print(f"Node {element} foi removido")
                    self.size-=1
                    found = True
                antecessor = pointer    
                pointer = pointer.next
        if not found:
            print(f"Node {element} não existe")

    def index(self,element):
        pointer = self.start
        i = 0
        while(pointer):
            if pointer.data == element:
                return i
            pointer = pointer.next
            i+=1
        return 'Falso'

    def push(self,element, index):
        #Condição para verificar se achou o elemento e se deu certo a ação de empurrar
        if self.start == None:
            print(f"Node {element} não existe")
        #Se não achar o elemento na lista retorn False
        elif index != "Falso":
                #Verificação se o index é do último elemento
                if index != self.size-1:
                        pointer = self.start
                        sucessor = self.start.next
                        while(pointer):
                            if pointer.data == element:
                                #o valor do pointer será empurrado para e próximo
                                pointer.data = sucessor.data
                                sucessor.data = element
                                print(f"Node {element} empurrado")
                                break
                            pointer = sucessor
                            sucessor = sucessor.next
                #SE ele for o último elemento deve printar isso
                else:
                    print(f"Não existe Node depois de {element}")
        else:
            print(f"Node {element} não existe")

       
    def pull(self,element,index):
        #Condição para verificar se achou o elemento e se deu certo a ação de empurrar
        if self.start == None:
            print(f"Node {element} não existe")
            #Se não achar o elemento na lista retorn False
        elif index != "Falso":
                #Verificação se o index é o primeiro elemento
                if index != 0:
                        pointer = self.start
                        sucessor = self.start.next
                        while(pointer):
                            if sucessor.data == element:
                                #ZAção de que o anterioro recebe o valor do sucessor
                                sucessor.data = pointer.data
                                pointer.data = element
                                print(f'Node {element} puxado')
                                break
                            pointer = sucessor
                            sucessor = sucessor.next
                else:
                    print(f"Não existe Node antes de {element}")
        else:
            print(f"Node {element} não existe")

    #Def feita pra printar a lista na tela
    def __repr__(self):
        r = ""
        pointer = self.start
        if pointer:
          while(pointer.next):
              r = r +  str(pointer.data) + '->'
              pointer = pointer.next
          r = r + str(pointer.data)
        return 'mapa:' + r

    def __str__(self):
        return self.__repr__()
    
linkedList = LinkedList()

while(True):
    action = str(input())
    if action == 'fim!':
        break
    id, ação = action.split(':')

    if ação == 'adicione-me!':
        linkedList.append(id)
        print(f"Node {id} adicionado")

    elif ação == "remova-me!":
        linkedList.remove(id)
    
    elif ação == "empurre-me!":
        index_elemento = linkedList.index(id)
        linkedList.push(id, index_elemento)

    elif ação == 'puxe-me!':
        index_elemento = linkedList.index(id)
        linkedList.pull(id, index_elemento)

print(linkedList)