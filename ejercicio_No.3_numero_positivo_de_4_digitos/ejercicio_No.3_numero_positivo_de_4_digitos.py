# Numero positivo de 4 digitos

print("---------------------------------------")
print("Calculo de un numero positivo de 4 digitos")
print("---------------------------------------")

#input
n=int(input("Ingrese el valor a saber: "))

#prossesing
if n>999:
    if n<= 9999:
      z="El número ingresado sí número  de cuatro digitos positivo"
    else:
      z="El número ingresado es un número positivo de mas de cuatro digitos"
else:
      if n>=0:
       z="El número ingresado es positivo menor a cuatro digitos"
      else:
        z="El numero ingresado es negativo"
  



#output
print("--------------------------------------")
print("---------------Resultados-------------")
print("¿N aplica con las condiciones?:"+(z))
#fin