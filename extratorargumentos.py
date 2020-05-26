class ExtratorArgumentosUrl:
    def __init__(self,url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("Url Invalida")

    @staticmethod
    def urlEhValida(url):
        if url:
            return True

        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem"
        buscamoedaDestino ="moedadestino"

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscamoedaDestino)

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem, moedaDestino


    def encontraIndiceInicial(self,moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) +1
