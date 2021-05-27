print("~"*45)
print(f"{'~'*5}Bem vindo ao jogo da adivinhação!!{'~'*5}")
print(f"{'~'*45}")
ask = True
while ask == True:
    numero_secreto = 42
    chute = float(input("Digite o seu numero: "))
    print("Voce digitou {}".format(chute))
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acerto = chute == numero_secreto
    if(numero_secreto == acerto):
        print('Você acertou !!')
    else:
        if(chute > maior):
            print("Voce errou! O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("Você errou!!O seu chute foi menor do que o numero secreto")
    stop = input("Você deseja tentar novamente? ")
    if stop.lower() == "n":
        ask == False
        break
    else:
        continue

    print("Fim de game.")
