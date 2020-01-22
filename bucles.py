
# Vector, array, coleccion, lista

lista = [0,1,2,3,4]

lista_o = [9,8,7,6,5]

lista_suma = []

lista_10 = range(10)
nombre = "Jv"

for i in lista_10:
    print(nombre)

index = 0
while index < len(lista):
    #programming time
    lista_suma.append(
        lista[index] + lista_o[index]
    )
    index = index + 1


print(lista_suma)


lista_suma = []

for i in range(len(lista)):
    lista_suma.append(
        lista[i] + lista_o[i]
    )

print(lista_suma)
