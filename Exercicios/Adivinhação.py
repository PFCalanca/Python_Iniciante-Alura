print("~"*45)
print(f"{'~'*5}Bem vindo ao jogo da adivinhação!!{'~'*5}")
print(f"{'~'*45}")


numero_secreto = 42
chute = float(input("Digite o seu numero: "))
print("Voce digitou", chute)
if(numero_secreto == chute):
    print('Você acertou !!')
else:
    if(chute > numero_secreto):
        print("Voce errou! O seu chute foi maior do que o numero secreto")
    elif (chute < numero_secreto):
        print("Você errou!!O seu chute foi menor do que o numero secreto")

print("Fim de game.")
