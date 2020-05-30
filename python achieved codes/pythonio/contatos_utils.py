import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding = 'latin_1'): #deixando o encoding padrao em latin_1
    contatos = []

    with open(caminho, encoding = encoding) as arquivo:
        leitor = csv.reader(arquivo) # encontra as posições no csv e quebrar

        for linha in leitor:
            id = linha[0]
            nome = linha[1]
            email = linha[2]

            contato = Contato(id,nome,email)
            contatos.append(contato) #colocando o contato na lista de contatos
    return contatos


def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo: #wb indica para abrir um arquivo binario em modo de escrita
        pickle.dump(contatos,arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode ="rb") as arquivo: #read bytes
        contatos = pickle.load(arquivo)

    return contatos

def contatos_para_json(contatos, caminho):
    with open(caminho, mode ="w") as arquivo:
        json.dump(contatos,arquivo, default = _contato_para_json) #objeto e arquivo

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo) #retorna uma lista com conteudos json

        for contato in contatos_json:
            c = Contato(contato['id'], contato['nome'], contato['email'])
            contatos.append(c)
        return contatos
