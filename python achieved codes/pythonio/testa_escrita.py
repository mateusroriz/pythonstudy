arquivo_contatos = open('contatos-escrita.csv', encoding = "latin_1", mode ='a+')

contatos = ['11,Carol,carol@dio\n',
            '12,dio,dio@dio\n',
            '13,jotaro,jotaro@jotaro\n']

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush() #escrevendo dados no arquivo antes do programa fechar

arquivo_contatos.seek(0) #procura no primeiro endereço do ponteiro
arquivo_contatos.write()

for linha in arquivo_contatos:
    print(linha)
