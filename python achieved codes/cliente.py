class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #usando property em um getter pra retornar letras maisculas na 1 letra
    def nome(self):
        print("chamando @property nome")
        return self.__nome.title()

    @nome.setter #usando property em um setter para modificar o nome
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
