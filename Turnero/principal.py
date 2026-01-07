import numeros

def preguntar():
    print("Bienvenido")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input("Elige un rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Elige un rubro valido")
        else:
            break

    numeros.decorador(mi_rubro)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Elige otro turno valido")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()



