class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        #Lista criada para o output em pos ordem
        self.root = None

    def rotate_right(self, parent):
         # child armazena o nó que será o novo nó parent
        child = parent.left
        # subtree armazena a subárvore à direita do novo nó parent 
        subtree = child.right

        # A subárvore à direita do novo nó parent agora se torna o antigo nó parent
        child.right = parent
        parent.left = subtree

        # Atualiza o parent do antigo filho da direita do parent para o child
        if subtree is not None:
            subtree.parent = parent

        # Atualiza o parent do child para o parent do antigo parent
        child.parent = parent.parent
        if parent.parent is None:
            # Se o antigo parent era a raiz, atualiza a raiz da árvore
            self.root = child
        else:
            # Atualiza o ponteiro do pai do antigo parent para o child
            if parent == parent.parent.left:
                parent.parent.left = child
            else:
                parent.parent.right = child

        # Atualiza o parent do antigo parent para o child
        parent.parent = child

        # Retorna o novo nó pai (child) após a rotação
        return child
    
    def rotate_left(self, parent):
        # O child armazena o parent.right, que sempre vai ser o root analisado,
        # e o subtree armazena o da esquerda do child
        child = parent.right
        subtree = child.left

        # O da esquerda ao child vira o parent e o da direita do parent vira o subtree assim rotacionando da direita para a esquerda
        child.left = parent
        parent.right = subtree

        # Atualiza o parent do antigo filho da esquerda do parent para o child
        if subtree is not None:
            subtree.parent = parent

        # Atualiza o parent do child para o parent do antigo parent
        child.parent = parent.parent
        if parent.parent is None:
            # Se o antigo parent era a raiz, atualiza a raiz da árvore
            self.root = child
        else:
            # Atualiza o ponteiro do pai do antigo parent para o child
            if parent == parent.parent.left:
                parent.parent.left = child
            else:
                parent.parent.right = child

        # Atualiza o parent do antigo parent para o child
        parent.parent = child

        return child
    

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.data:
                    if current.left is None:
                        current.left = Node(value)
                        current.left.parent = current
                        break
                    else:
                        current = current.left
                elif value > current.data:
                    if current.right is None:
                        current.right = Node(value)
                        current.right.parent = current
                        break
                    else:
                        current = current.right
                else:
                    # Valor já existe na árvore, você pode decidir o que fazer nesse caso.
                    break

    def toTop(self, node):
        while self.root != node:
            parent = node.parent
            father_parent = parent.parent

            # Se não tiver o pai do parent, significa que somente há duas alturas na avore e necessita de uma rotação simples
            if father_parent:

                # Se tiver um no a esquerda do pai do parent tem a possibilidade de ocorrer as rotações duplas e a simples para a direita 
                if father_parent.left:

                    # ROTAÇÃO SIMPLES PARA A DIREITA
                    if parent.left == node and father_parent.left == parent:
                        self.rotate_right(parent)
                    else:
                        # ROTAÇÃO DUPLA PARA A DIREITA LF
                        if parent.right == node and father_parent.left == parent:
                            father_parent.left = self.rotate_left(parent)
                            self.rotate_left(father_parent)
                        # ROTAÇÃO DUPLA PARA A ESQUERDA RL
                        elif parent.left == node and father_parent.right == parent:
                            father_parent.right = self.rotate_right(parent)
                            self.rotate_left(father_parent)

                if father_parent.right:
                    # ROTAÇÃO SIMPLES PARA A ESQUERDA
                    if parent.right == node and father_parent.right == parent:
                        self.rotate_left(parent)

                    # Se não acontecer a rotação simples, abre a verificação se tem os nos necessarios para verificar as duplas
                    else:
                        # ROTAÇÃO DUPLA PARA A DIREITA LF
                        if parent.right == node and father_parent.left == parent:
                            father_parent.left = self.rotate_left(parent)
                            self.rotate_right(father_parent)
                        # ROTAÇÃO DUPLA PARA A ESQUERDA RL
                        elif parent.left == node and father_parent.right == parent:
                            father_parent.right = self.rotate_right(parent)
                            self.rotate_left(father_parent)
            else:
                # Significa que tem somente duas altuas na arvore e tem que fazer a rotação simples
                if parent.left:
                    return self.rotate_right(parent)
                elif parent.right:
                    return self.rotate_left(parent)
           
        return node
    
    def search(self, value, node=None):
        current = self.root
        index = 0

        while current:
            if value == current.data:
                if node is None:
                    return index
                else:
                    self.toTop(current)
                    return index
            elif value < current.data:
                current = current.left
            else:
                current = current.right
            index += 1    

        return -1

bst = BinaryTree()
while True:
    try:
        commands = input()
        if not commands:
            break
        command, node = commands.split()
        if command == "ADD":
            bst.insert(int(node))
            print(bst.search(int(node)))
        elif command == "SCH":
            print(bst.search(int(node),True))
    except EOFError:
        break