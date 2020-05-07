import random

def jogar():

    palavra_secreta = carregar_arquivo_palavras()

    letras_acertadas = ['_' for letra in palavra_secreta] # adicionando _ para cada caractere em uma lista #this is the list comprehention property
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual letra?").strip().lower() #pegando letra do usuário e retirando espaços com strip()

        if(chute in palavra_secreta):
            marcando_chutes_acertados(chute,letras_acertadas,palavra_secreta)
        else:
            erros +=1

        enforcou = erros == 7   #se chegou a 6 erros enforcou vira true
        acertou = "_" not in letras_acertadas #acerta quando nao houver letras faltando na palavra secreta
        print(letras_acertadas)

    if(acertou):
        print("Parabens você acertou a palavra")
    else:
        imprime_mensagem_perdedor(palavra_secreta)



def carregar_arquivo_palavras():
    arquivo = open("palavras.txt", "r")

    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha) #adicionando as palavras do arquivo para uma lista

    arquivo.close()

    numero_palavra = random.randrange(0,len(palavras)) #escolhendo um numero aleatorio das posições de palavras na string
    palavra_secreta = palavras[numero_palavra].lower()
    return palavra_secreta

def marcando_chutes_acertados(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta: #iterando cada caractere da palavra secreta
        if(chute.lower() == letra.lower()):
            letras_acertadas[index] = letra # se acertar colocar a letra acertada na lista letras_acertadas
        index +=1 #aumentando o index a cada loop

def imprime_mensagem_perdedor(palavra_secreta):
    print(" Você perdeu!")
    print("A palavra era {}".format(palavra_secreta))


if(__name__ == "__main__"): #se esse programa for o principal rodar isso
    jogar()
