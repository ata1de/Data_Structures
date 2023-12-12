import math

instructions = int(input())
instructions1 = instructions
instructions2 = instructions
pc1, capacity1, algoritmo1, complex1 = input().split(" - ")
pc2, capacity2, algoritmo2, complex2 = input().split(" - ")

if complex1 == "2n^2":
  instructions1 = 2*(instructions1**2)
elif complex1 == "n.logn":
  instructions1 = instructions1*(math.log(instructions1))
elif complex1 == "2^n": 
  instructions1 = 2**instructions1

vel1 = float("{:.2f}".format(instructions1/int(capacity1)))

if complex2 == "2n^2":
  instructions2 = 2*(instructions2**2)
elif complex2 == "n.logn":
  instructions2 = instructions2*(math.log10(instructions2))
elif complex2 == "2^n":
  instructions2 = 2**instructions2

vel2 = float("{:.2f}".format(instructions2/int(capacity2)))
  
print(f"Velocidade do {pc1}: {vel1:.2f} segundos")
print(f"Velocidade do {pc2}: {vel2:.2f} segundos")
if vel1<vel2:
  print(f"O {pc1} foi mais rápido")
else:
  print(f"O {pc2} foi mais rápido")
  