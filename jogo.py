import forca
import adivinhacao
print("Escolha o seu jogo")
print("(1)forca (2) adivinhação")

escolha = int(input('Qual jogo?'))

if(escolha == 1):
    print("jogando forca")
    forca.jogar()
elif(escolha ==2):
    print("jogando advinhação")
    adivinhacao.jogar()
