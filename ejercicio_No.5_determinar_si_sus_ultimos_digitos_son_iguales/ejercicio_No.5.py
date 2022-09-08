#Ejercicio No.5 determine si sus dos últimos dígitos son iguales.

print("------------------------------------------------------------")
print("------LOS DOS ULTIMOS DIGITOS DE UN NUMERO SON IGUALES------")
print("------------------------------------------------------------")

#Input

n=(int(input("ingrese el valor a comprobar: ")))

#prossesing

Z=n%100
X=Z%10
Y=Z//10

if X==Y:
    Respuesta="sus dos ultimos digitos si son  iguales"
else:
    Respuesta="sus dos ultimos digitos no son iguales"

#output

print("------------------")
print("-----Respuesta----")
print(+(Respuesta))