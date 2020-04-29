print("Jogo de advinhação!")

numero_secreto = 42

chute_str = input("digite o seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str) #int() convert the str to int so it returns no errors

if(numero_secreto == chute):
    print("acertou")
else:
    print('ERROU!')
