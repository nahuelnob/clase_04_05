"""
2) Escribe un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar,
debe repetirse el proceso hasta que lo introduzca correctamente.
"""

n = 0
while n % 2 == 0:
  n = int(input("Elija un numero impar: "))
  if n % 2 == 0:
    print(f"{n} es par, vuelve a elejir")
  elif n % 2 != 0:
    print(f"Exelente {n} es un número impar!!!")