# 🔋 Stack
O código a seguir representa parcialmente uma pilha. Para que ele funcione corretamente você deve implementar os métodos push, responsável por adicionar novos elementos a pilha, e o método pop, responsável por revomer os elementos da pilha. ATENÇÃO: Você deve usar a classe Node do código para armazenar os elementos da pilha, e não listas built-in de Python.

## Code
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        # ______________Complete aqui______________

    def pop(self):
        # ______________Complete aqui______________

    def get(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next_node
        return elements


def main():
    stack = Stack()

    elements = input()

    for element in elements.split():
        stack.push(element)

    print(f"Pilha: {stack.get()}")

    for _ in range(len(elements.split())):
        popped_element = stack.pop()
        print(f"Removido: {popped_element}")
        print(f"Pilha: {stack.get()}")

if __name__ == "__main__":
    main()
```

### Inputs
Uma lista separada por espaços:
```
1 2 3 4 5
```

### Outputs
Uma sequência que mostra a pilha e o item remvido:
```
Pilha: ['5', '4', '3', '2', '1']
Removido: 5
Pilha: ['4', '3', '2', '1']
Removido: 4
Pilha: ['3', '2', '1']
Removido: 3
Pilha: ['2', '1']
Removido: 2
Pilha: ['1']
Removido: 1
Pilha: []
```