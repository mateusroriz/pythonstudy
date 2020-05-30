arquivo = open("contatos-escrita.csv", encoding= 'latin_1', mode='a+')


print(type(arquivo.buffer))

contato = bytes("15,xôtaro, jotaro@jotaro", 'latin_1')
arquivo.buffer.write(contato)

texto_em_bytes = bytes("esse é um texto em bytes", "latin_1")
#print(texto_em_bytes)
arquivo.close()
