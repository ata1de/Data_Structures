class Node:
  def __init__(self,valor, groupe):
    self.valor = valor
    self.next = None
    self.groupe = groupe

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def append(self, element, groupe):
        if self.start != None:
            pointer = self.start
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element, groupe)
        else:
            self.start = Node(element, groupe)
        self.size+=1

    def sort_linked(self, list):
        temporary_list = []
        pointer = self.start
        while(pointer):
            temporary_list.append(pointer.data)
            pointer = pointer.next
        
        return sorted(temporary_list), self.start.groupe

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    # Função de inserir o elemento na hash table
    def insert(self,key,value):
        if self.table[key-1] is None:
            # Criando uma linked list para cada index e adicionando os nomes nela
            lista_linkada = LinkedList()
            lista_linkada.append(value, key)
            self.table[key-1] = lista_linkada
        else:
            # Se o index já tiver uma linked list ele somente adiciona o nome nela
            lista_linkada = self.table[key-1]
            lista_linkada.append(value, key)

    def create_groups(self, list, groupe):
          sublistas = [list[i: i + groupe] for i in range(0, len(list), groupe)]
          return sublistas



    def sorted_print(self):
        printed_list = []
        for lindked in self.table:
            # Se tiver alguma LinkedList ele irá ordena-la e depois agrupa-la
            if lindked:
                # Ordenação da lista
                lindked_sorted, groupe = lindked.sort_linked()
                # Separação por grupos dependendo do atributo groupe do head da LinkedList
                subslists = self.create_groups(lindked_sorted, groupe) 
                for lists in subslists:
                    printed_list.append(lists)

        return printed_list

  
hash_table = HashTable()

while True:
    try:
        pessoa, tamanho_grupo = input().split()
        hash_table.insert(int(tamanho_grupo), pessoa) 
    except EOFError:
       break

print(hash_table.sorted_print())




    