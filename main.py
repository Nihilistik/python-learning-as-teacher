
LIMITE_SUPERIOR_ANOS = 5000
ano_inferior = 1400

ano_usuario_input = int(input("Introduce un año del 1400 al 5000: "))

for ano_usuario in range(int(ano_usuario_input), LIMITE_SUPERIOR_ANOS):

    if ano_usuario < LIMITE_SUPERIOR_ANOS and ano_usuario > ano_inferior:

        if ano_usuario % 4 == 0:
            if ano_usuario % 100 != 0 or (ano_usuario % 400 == 0 and ano_usuario % 100 == 0):
                print("{0}/{1} Es bisiesto".format(ano_usuario, LIMITE_SUPERIOR_ANOS))
                print(f"{ano_usuario}/{LIMITE_SUPERIOR_ANOS} Es bisiesto")
            else:
                print(f"{ano_usuario} No es bisiesto")
        else:
            print(f"{ano_usuario} No es bisiesto")


    else:
        print("Fecha no disponible")

exit()