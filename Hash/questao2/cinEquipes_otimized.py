class Node:
    def __init__(self, valor, groupe):
        self.valor = valor
        self.next = None
        self.groupe = groupe

class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def append(self, element, groupe):
        new_node = Node(element, groupe)
        if self.start is None:
            self.start = new_node
        else:
            pointer = self.start
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
        self.size += 1

    def sort_linked(self):
        temporary_list = []
        pointer = self.start
        while pointer:
            temporary_list.append(pointer.valor)
            pointer = pointer.next
        return sorted(temporary_list), self.start.groupe

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def insert(self, key, value):
        if self.table[key - 1] is None:
            self.table[key - 1] = LinkedList()
        self.table[key - 1].append(value, key)

    def create_groups(self, lista, groupe):
        return [lista[i: i + groupe] for i in range(0, len(lista), groupe)]

    def sorted_print(self):
        printed_list = []
        for linked in self.table:
            if linked:
                linked_sorted, groupe = linked.sort_linked()
                sublists = self.create_groups(linked_sorted, groupe)
                printed_list.extend(sublists)
        return printed_list

hash_table = HashTable()

while True:
    try:
        pessoa, tamanho_grupo = input().split()
        hash_table.insert(int(tamanho_grupo), pessoa)
    except EOFError:
        break

print(hash_table.sorted_print())
