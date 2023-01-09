"""
1) Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""

n1 = 0
n2 = 0
print("Realicemos operaciones matemáticas")
operacion = ""

while operacion != "*":
  n1 = int(input("Ingrese el 1er número: "))
  n2 = int(input("Ingrese el 2do número: "))
  operacion = input("¿Qué operación desea realizar: + | - | * ? (el programa termina cuando elige *): ")
  if operacion == "+":
    resultado = n1 + n2
    print(f"su resultado es {resultado}")
  elif operacion == "-":
    resultado = n1 - n2
    print(f"su resultado es {resultado}")
  elif operacion == "*":
    resultado = n1 * n2
    print(f"su resultado es {resultado}")