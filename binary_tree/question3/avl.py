class Node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

class AVLTree:
    def __init__(self):
        #Lista criada para o output em pos ordem
        self.avl = []
        self.duplicates =[]
        self.root = None


    #O balanceamento é feito a partir da subtração da subarvore à esquerda da direita
    def balance_factor(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return left_height - right_height
    

    def rotate_right(self, parent):
        # child armazena o nó que será o novo nó parent
        child = parent.left
        # subtree armazena a subárvore à direita do novo nó parent 
        subtree = child.right
        # A subárvore à direita do novo nó parent agora se torna o antigo nó parent
        child.right = parent
        # A subárvore à esquerda do antigo nó parent  agora se torna a subárvore à direita do novo nó parent
        parent.left = subtree

        # Por último, atualiza as alturas de ambos os nós envolvidos na rotação
        self.update_height(parent)
        self.update_height(child)
        # Retorna o novo nó pai (child) após a rotação
        return child
    
    def rotate_left(self, parent):
        #O child armazena o  parent.right, que sempre vai ser o root analisado, eo subtree armazena o da esquerda do child
        child = parent.right
        subtree = child.left
        #O da esquerda ao child vira o parent e o da direita do parent vira o subtree assim rotacionando da direita para a esquerda
        child.left = parent
        parent.right = subtree

        #Por último, atualiza as alturas de ambas as subarvores
        self.update_height(parent)
        self.update_height(child)
        return child
    
    def height(self, node):
        if node is None:
            return 0
        return node.height
    
    #A altura é atualizada aqui, somando o maior entre suas subarvores
    def update_height(self, node):
        if node is not None:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            node.height = 1 + max(left_height, right_height)

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            self.duplicates.append(data)  # No duplicate keys allowed
        
        self.update_height(root) #Atualizamos os valores da subarvore e da arvore ao inserirmos um elemento
        balance = self.balance_factor(root)#E aqui fazemos o balanceamento para verificar se esta balanceada

        # Se a rotação for > 1, significa que o a subarvore da esquerda está maior que o da direita
        if balance > 1:
            # Se o elemento for menor que o elemento a esquerda do root, rotaciona da esqurda para a direita essa subarvore
            if data < root.left.data:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Se a rotação for < -1, significa que o a subarvore da direita está maior que o da esquerda
        if balance < -1:
            # aqui está a verificação se o elemento é maior que o filho da direita do root, e assim rotacionando da diretia p esquerda
            if data > root.right.data:
                return self.rotate_left(root)
            else:
                # E aqui o oposto do cenário anterior
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_key(self, data):
        self.root = self.insert(self.root, data)

    #Percurso em ordem
    def inorder_traversal(self, node =None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)

        self.avl.append(node.data)

        if node.right:
            self.inorder_traversal(node.right)

    #Utiliza o percurso em ordem e depois organiza em uma lista
    def display_posOrdem(self):
        self.inorder_traversal()
        return self.avl
    
    def display_duplicates(self):
        return self.duplicates

#Input 
teachsH, teachsC = input().split() #correspondente ao números de aulas de Hogwarts e Cin, respectivamente
knowledge_Hogwarts = input().split() #Conhecimentos de Hogwarts e o do Cin abaixo
knowledge_CIN = input().split()
limit_hours = int(input()) #Limite de horas do vira tempo
#Vai ser o tamanho da avl total
size = len(knowledge_Hogwarts) + len(knowledge_CIN)

avl_tree = AVLTree() #criação da avl
result = 0 # meu output
#Inserindo os valores do conhecimento das aulas de Hogwarts e Cin na avl
for values in knowledge_Hogwarts:
    avl_tree.insert_key(int(values))

for values in knowledge_CIN:
    avl_tree.insert_key(int(values))

#Criando uma variável para supostar o pós ordem da avl
avl = avl_tree.display_posOrdem()
duplicates = avl_tree.display_duplicates()
list_total = avl + duplicates
list_total.sort()
count = 0
#Reitero por toda a lista de elementos, diminuindo o limite de horas e somando o conhecimento
for elements in list_total[::-1]:
    if count < limit_hours:
        result+=elements
        count+=1
print(f"valor total de conhecimento: {result}")
