def jogar():
    print("Bem vindo ao jogo da forca")

    palavra_secreta = "Python"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra?").strip() #pegando letra do usuário e retirando espaços com strip()


        index = 0
        for letra in palavra_secreta: #iterando cada caractere da palavra secreta
            if(chute.lower() == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra,index))
            index +=1 #aumentando o index a cada loop

        print("jogando...")

    print("TODO: Fim do jogo")

if(__name__ == "__main__"): #se esse programa for o principal rodar isso
    jogar()
