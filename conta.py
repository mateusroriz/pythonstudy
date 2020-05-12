
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
        
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property #usando property em um getter pra retornar o valor do limite
    def limite(self):
        return self.__limite

    @limite.setter #usando property em um getter pra modificar o valor do limite
    def limite(self, limite):
        self.__limite = limite
