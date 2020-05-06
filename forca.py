def jogar():
    print("Bem vindo ao jogo da forca")

    palavra_secreta = "python".lower()
    letras_acertadas = ['_' for letra in palavra_secreta] # adicionando _ para cada caractere em uma lista #this is the list comprehention property

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?").strip().lower() #pegando letra do usuário e retirando espaços com strip()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta: #iterando cada caractere da palavra secreta
                if(chute.lower() == letra.lower()):
                    letras_acertadas[index] = letra # se acertar colocar a letra acertada na lista letras_acertadas
                index +=1 #aumentando o index a cada loop
        else:
            erros +=1

        enforcou = erros == 6   #se chegou a 6 erros enforcou vira true
        acertou = "_" not in letras_acertadas #acerta quando nao houver letras faltando na palavra secreta
        print(letras_acertadas)

    if(acertou):
        print("Parabens você acertou a palavra")
    else:
        print("Você perdeu")

    print("Fim do jogo")

if(__name__ == "__main__"): #se esse programa for o principal rodar isso
    jogar()
