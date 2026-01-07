class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre}, {self.apellido}\nBalance de cuenta {self.numero_cuenta}; ${self.balance}"

    def depositar(self, monto_depositado):
        self.balance += monto_depositado
        print("Deposito aceptado")

    def retirar(self,monto_retirado):
        if self.balance >= monto_retirado:
            self.balance -= monto_retirado
            print("Retirando monto")
        else:
            print("El monto no puede retirar")

def crear_cliente():
    nombre_cl = input("Ingrese el nombre del cliente: ")
    apellido_cl = input("Ingrese apellido del cliente: ")
    numero_cuenta = input("Ingrese el numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elige: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Ingrese el monto de depositar: "))
            mi_cliente.depositar(monto_dep)

        elif opcion == 'R':
            monto_ret = int(input("Ingrese el monto de retirar: "))
            mi_cliente.retirar(monto_ret)

        print(mi_cliente)
    print("Gracias")

inicio()







