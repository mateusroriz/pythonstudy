from extratorargumentos import ExtratorArgumentosUrl
'''
argumento = "moedaorigem=real"

listaargumento = argumento.split("=")
print(listaargumento)

url = ""
'''

#url = "moedaorigem=real&moedadestino=dolar"

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, MoedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(MoedaDestino, moedaOrigem, valor )
