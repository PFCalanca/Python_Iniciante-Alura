print("~"*45)
print(f"{'~'*5}Bem vindo ao jogo da adivinhação!!{'~'*5}")
print(f"{'~'*45}")

numero_secreto = 42
rodada = 1
tentativas = 3
total_tentativas= 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativas {} de {}".format(rodada,total_tentativas))
    chute = float(input("Digite o seu número entre 1 ate 100:\n "))
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acerto = chute == numero_secreto

    print("Voce digitou", chute)
    if(chute < 1 or chute > 100):
        print("Você deveria digitar um numero valido!!")
        continue
    if(acerto):
        print('Você acertou !!\n')
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior do que o numero secreto\n")
        elif (menor):
            print("Você errou!!O seu chute foi menor do que o numero secreto\n")

    print("Fim de game.")
    rodada += 1
