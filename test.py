HOMBRE = 'hombre'
MUJER = 'mujer'

lista_grupo_mujeres = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',)
lista_grupo_hombres = ('o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', )

nombre = input("Nombre: ")
sexo = input("Sexo: ")

primer_letra = nombre[0].lower()
sexo = sexo.lower()

if (
        sexo == MUJER and primer_letra in lista_grupo_mujeres
) or (
        sexo == HOMBRE and primer_letra in lista_grupo_hombres
):
    print("GRUPO A")
else:
    print("GRUPO B")