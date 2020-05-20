arquivo_contatos = open('contatos.csv', encoding='latin_1')


for linha in arquivo_contatos:
    print(linha, end='')
