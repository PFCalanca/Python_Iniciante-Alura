import random
def jogar_advinhacao():
    print("~"*45)
    print(f"{'~'*5}Bem vindo ao jogo da adivinhação!!{'~'*5}")
    print(f"{'~'*45}")

    numero_secreto= random.randrange(1,101)
    total_tentativas= 3
    pontos = 1000

    print("Qual nivel de dificuldade?\n",numero_secreto)
    print("(1)-Facil (2)-Médio (3)-Difícil\n ")

    nivel = int(input("Defina o nível :"))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

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
            print('Você acertou e fez {} pontos!!\n'.format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto\n")
            elif (menor):
                print("Você errou!!O seu chute foi menor do que o numero secreto\n")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
        rodada += 1

    print("Fim de game.")
