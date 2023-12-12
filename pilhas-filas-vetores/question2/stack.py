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
        node = Node(data)
        node.next_node = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
          return None
        pop_data = self.top.data
        self.top = self.top.next_node
        return pop_data
    
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