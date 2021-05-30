def jogar_forca():
    print("~"*45)
    print(f"{'~'*5}Bem vindo ao forca!!{'~'*5}")
    print(f"{'~'*45}")

    palavra = input("Escolha uma palavra: ")
    palavra_secreta = palavra.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    erros = 0

    enforcou = False
    acertou = False
    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Escolha uma letra: \n")
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

if(__name__=="__main__"):
    jogar_forca()
