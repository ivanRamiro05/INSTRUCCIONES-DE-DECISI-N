# Ejercicio No.8 raices de una ecuacion de segund grado

print("---------------------------------------------")
print("--resolucion de ecuaciones de segundo nivel--")
print("---------------------------------------------")

#input
from math import sqrt
A=int(input("ingresar el valor de a: "))
B=int(input("ingresasr el valor de b: "))
C=int(input("ingresasr el valor de c: "))

#prossesing
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
  
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)

#output
print("Las soluciones de la ecuación son:")
print(x1)
print(x2)