
class Conta:

    def __init__(self, numero, titular, saldo, limite): #self é a referencia para encontrar o objeto quando criado
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor , destino):
        self.sacar(valor)
        destino.depositar(valor)
