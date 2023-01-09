"""
4) Escribe un programa que pida al usuario cuantos números quiere introducir.
Luego lee todos los números y realiza una media aritmética.
"""

print("Vamos a realizar una media aritmética.") 
cant_numeros = int(input("¿Cuantos números vamos a usar?: "))
numeros = []
while cant_numeros != len(numeros):
  numeros.append(int(input("ingrese numeros: ")))
  media = sum(numeros)/cant_numeros
else:
  print(f"La media aritmética es = {media}")