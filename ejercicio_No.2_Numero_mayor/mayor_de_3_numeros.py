#EJERCICIO No 2 MAYOR DE 3 NUMEROS 

print("--------------------------------")
print("-------MAYOR DE 3 ENTEROS-------")
print("--------------------------------")

#input
a=int(input("ingrese el valor de a:  "))
b=int(input("ingrese el valor de b:  "))
c=int (input("ingrese el valor de c: "))

#prossesing
if a>b:
    if a>c:
        mayor=a
    else:
      mayor=c
else:
    if b>c:
        mayor=b
    else:
        mayor=c

#output
print("---------------------------------------------------")
print("-----------------RESULTADOS------------------------")
print("El mayor entre " + str(a) + ", " + str(b) + " y " + str(c) + " es: " + str(mayor))

#finish
