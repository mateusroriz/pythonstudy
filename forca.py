def jogar():
    print("Bem vindo ao jogo da forca")

    palavra_secreta = "Python"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?").strip() #pegando letra do usuário e retirando espaços com strip()

        index = 0
        for letra in palavra_secreta: #iterando cada caractere da palavra secreta
            if(chute.lower() == letra.lower()):
                letras_acertadas[index] = letra # se acertar colocar a letra acertada na lista letras_acertadas
            index +=1 #aumentando o index a cada loop

        print(letras_acertadas)

    print("TODO: Fim do jogo")

if(__name__ == "__main__"): #se esse programa for o principal rodar isso
    jogar()
