print("Jogo de advinhação!")

numero_secreto = 42
total_de_tentativas = 5

while(total_de_tentativas > 0):
    #print("Você tem mais: {} ", total_de_tentativas, "tentativas")
    print("Você tem mais: {}  tentativas".format (total_de_tentativas))
    chute = int(input("digite o seu numero: ")) #converting the str to int right in the input

    if(chute):
        total_de_tentativas -=1

    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute> numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        exit()
    else:
        if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
        elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
