#minutos de llamada Ejercio No 1

print("-----------------------------")
print("TOTAL A PAGAR POR UNA LLAMADA")
print("-----------------------------")

#input

m=int(input("Cantidad de minutos usados: "))

#prossesing

if m>3:
    mayor=300+50*(m-3)
else:
    mayor=300
#output

print("--------Resultados---------")
print("Total a pagar:$ " +str(mayor))
#fin