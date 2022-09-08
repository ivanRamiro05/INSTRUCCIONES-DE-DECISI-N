#Ejercicio No.6dígitos es un número de 1 dígito.
 
print("------------------------------------------------------------")
print("------LOS DOS ULTIMOS DIGITOS DE UN NUMERO SON IGUALES------")
print("------------------------------------------------------------")

#Input

n=(int(input("ingrese el valor a comprobar: ")))

#prossesing

Z=n%100
X=Z%10
Y=Z//10
A=X+Y
if A//10:
    R="la suma de los dos ultimos digitos es de dos digitos"
else:
     R="la suma de los dos ultimos digitos es de un digito"

#output
print("------------------------")
print("------Respuesta---------")
print(str(R))