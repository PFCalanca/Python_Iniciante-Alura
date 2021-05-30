import Adivinhação
import forca
print("*********************************")
print("*******Escolha o seu jogo********")
print("*********************************")




def escolha_jogo():
    print(" (1)-Forca (2)-Adivinhação\n")

    jogo = int(input("Qual jogo?"))

    if (jogo ==1):
        print("Jogando Forca!!")
        forca.jogar_forca()
    elif(jogo==2):
        print("Jogando Adivinhação")
        Adivinhação.jogar_advinhacao()


if(__name__=="__main__"):
    escolha_jogo()
