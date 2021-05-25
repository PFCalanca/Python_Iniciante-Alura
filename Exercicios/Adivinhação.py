print("~"*45)
print(f"{'~'*5}Bem vindo ao jogo da adivinhação!!{'~'*5}")
print(f"{'~'*45}")


maior = chute > numero_secreto
menor = chute < numero_secreto
acerto = chute == numero_secreto

numero_secreto = 42
chute = float(input("Digite o seu numero: "))
print("Voce digitou", chute)
if(numero_secreto == acerto):
    print('Você acertou !!')
else:
    if(chute > maior):
        print("Voce errou! O seu chute foi maior do que o numero secreto")
    elif (menor):
        print("Você errou!!O seu chute foi menor do que o numero secreto")

print("Fim de game.")
