import Adivinhação
import forca
print("~"*45)
print(f"{'~'*5}Escolha o seu jogo!!{'~'*5}")
print(f"{'~'*45}")



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
