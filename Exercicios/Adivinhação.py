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
        print("Voce errou!")

print("Fim de game.")
