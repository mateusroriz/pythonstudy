try:
    with open('contatos.csv', encoding='UTF-8') as arquivo_contatos: #opening the file just when we are using it then closing it
        for linha in arquivo_contatos:
            print(linha, end='')

except FileNotFoundError:
    print("Arquivo não encontrado")

except PermissionError:
    print("Sem permissão de escrita")
