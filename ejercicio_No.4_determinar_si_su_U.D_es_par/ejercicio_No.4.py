# Ejercicio No.4 determine si si último dígito es un número par.

print("---------------------------")
print("-------BIENVENIDO----------")
print("---------------------------")

#input

N=(int(input("Ingrese el valor a conocer: ")))

#prossesing

N=N%10
if N//2:
    Z="EL ultimo digito es impar"
else:
     Z="El numero ingresado es par"

#output
print("-------------------")
print("----Resultado------")
print(str(Z))

#fin

