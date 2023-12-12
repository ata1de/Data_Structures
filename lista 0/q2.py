class Animal:    
    def __init__(self):
        self.listaAnimais = []

    def cadastro(self,local, raca, data):
        self.listaAnimais.append((local, raca, data))

    def imprimeRelatorio(self):
        for animal in self.listaAnimais:
            print(f"Local: {animal[0]}\nRaça: {animal[1]}\nData: {animal[2]}\n")

    def dataInteresse(self,data):
        diaI, mesI, anoI = data.split("/")

        for animal in self.listaAnimais:
            dia, mes, ano = animal[2].split("/")

            if int(ano) > int(anoI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

            elif int(ano) == int(anoI) and int(mes) > int(mesI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()
                
            elif int(ano) == int(anoI) and int(mes) == int(mesI) and int(dia) > int(diaI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

    def removerAnimal(self,raca, data):
        self.listaAnimais = [animal for animal in self.listaAnimais if (animal[1] != raca or animal[2] != data)]


serviço = Animal()

while True:
    entrada = input()

    if entrada == "1":
        registros = input().split()
        serviço.cadastro(registros[0], registros[1], registros[2])
        
    elif entrada == "2":
        serviço.imprimeRelatorio()
        
    elif entrada == "3":
        data = input()
        serviço.dataInteresse(data)
        
    elif entrada == "4":
        remover = input().split()
        serviço.removerAnimal(remover[0], remover[1])
        
    elif entrada == "5":
        break
    
