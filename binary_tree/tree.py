class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self,data = None, node= None):
        self.index = 0
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def insert(self, value):
        parent = None
        root = self.root
        while(root):
            parent = root
            if value<root.data:
                root = root.left
            else:
                root = root.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self,value):
        return self._search(value,self.root)
    
    def _search(self, value, root):
        # Verifica se a árvore ou subárvore está vazia ou se encontrou o valor
        if root is None or root.data == value:
            return BinaryTree(value)
        # Procura na subárvore à esquerda se a chave é menor
        if root.data > value:
            return self._search(value,root.left)
        # Procura na subárvore à direita se a chave é maior
        return self._search(value, root.right)
        
    # percurso em ordem travessa, ou seja, buscando os nós da esquerda a direita
    def inorder_traversal(self, size,node= None):
        self.index+=1
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(size,node.left)

        if self.index == size:
            print(node, end='')
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(size,node.right)

    # Percurso Pós Ordem, analisando os nós da esquerda para a direita,e printando-os quando não tiver mais filhos à esquerda
    def postorder_traversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(self, node.left)
        if node.right:
            self.postorder_traversal(self, node.right)
        print(node)


    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print(node)
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)
        else:
            print(node)
        
binary_tree = BinaryTree()

sequence = input().split()
for number in sequence:
    binary_tree.insert(int(number))
binary_tree.inorder_traversal(len(sequence))