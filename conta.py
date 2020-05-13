
class Conta:
    #construtor
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

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar #return true or false

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

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

    @staticmethod
    def codigo_banco(): #metodo estatico é da classe, nao precisa do objeto
        return "001"

    @staticmethod
    def codigos_bancos(): #metodo estatico é da classe, nao precisa do objeto
        return {"BB" : "001", "Caixa" : "104", "Bradesco": "237"}
