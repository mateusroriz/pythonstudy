from extratorargumentos import ExtratorArgumentosUrl
'''
argumento = "moedaorigem=real"

listaargumento = argumento.split("=")
print(listaargumento)

url = ""
'''

#url = "moedaorigem=real&moedadestino=dolar"
url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar"
argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem, MoedaDestino = argumentosUrl.extraiArgumentos()
print(moedaOrigem, MoedaDestino)

#index = url.find("moedadestino") + len("moedadestino") +1
#substring = url[index:]
#print(index)
