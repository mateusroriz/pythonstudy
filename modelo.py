class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self): #usando proprety para retornar atributos privados para nao precisar modificar todos os lugares do codigo que usam likes e nomes
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes +=1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes +=1



vingadores = Filme("Vigadores - Guerra Infinita", 2018, 160)

westworld = Serie("Westworld", 2017, 2)


westworld.dar_like()
vingadores.dar_like()
vingadores.dar_like()

print(vingadores.nome, vingadores.likes)
print(westworld.nome, westworld.ano, westworld.temporadas, westworld.likes)
