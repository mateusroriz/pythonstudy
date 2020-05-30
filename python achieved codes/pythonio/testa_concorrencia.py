contato_dio = '11,dio,dio@dio\n'
contato_jotaro = '12,jotaro,jotaro@jotaro\n'

with open('contatos-escrita.csv', encoding = 'latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_dio)
with open('contatos-escrita.csv', encoding = 'latin_1', mode='a') as arquivo2:
    arquivo2.write(contato_jotaro)
