"""
5) Escribe un programa que pida al usuario un número entero del 0 al 9,
y que mientras el número no sea correcto se repita el proceso.
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
"""

num = list(range(0,10,1))
x = int(input("Escoja un número entero entre el 0 y el 9: "))
for i in num:
  while i != x:
    if x in num: 
      break
    x = int(input("Incorrecto, escoge otro: "))
print(f"Exelente, has elegido el {x} que cumple con los requisitos") 