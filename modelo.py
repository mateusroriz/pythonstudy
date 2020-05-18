class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self): #usando proprety para retornar atributos privados para nao precisar modificar todos os lugares do codigo que usam likes e nomes
        return self._likes

    def dar_like(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self): #representando objeto como texto
        return (f'{self._nome} - {self.ano} - {self._likes} Likes')

class Filme(Programa): #herdando da classe Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #super chama a classe mae nesse caso o inicializador dela
        self.duracao = duracao

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.duracao} Min - {self._likes} Likes')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano) #super chama qualquer metodo da classe mae
        self.temporadas = temporadas

    def __str__(self):
        return (f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes')


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self): #retornando os programas dentro da playlist
        return self._programas

    @property
    def tamanho(self): #retornando a quantidade de objectos na playlist
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
westworld = Serie('westworld', 2018, 2)
drive = Filme("Drive", 2015, 100)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

westworld.dar_like()
westworld.dar_like()

filmes_e_series = [vingadores, westworld, drive]
playl_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playl_fim_de_semana.listagem)}")

for programa in playl_fim_de_semana.listagem:
    print(programa)

print(f"Existe dentro da playlist:{drive in playl_fim_de_semana.listagem}")
