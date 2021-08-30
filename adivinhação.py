import random
print ("*********************************")
print ("Bem vindo ao Jogo da Adivinhação!")
print ("*********************************")

numero_secreto = random.randrange (1,101)
total_de_tentativas = 0
pontos = 1000

print ("Qual o nível do jogo?", numero_secreto)
print ("(1) Fácil (2) Médio (3) Difícil")

nível = int(input("Escolha o nível: "))
if (nível == 1):
    total_de_tentativas = 20
elif (nível == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Usuário, digite um número entre 1 e 100: ")
    print ("Você digitou ", chute_str)
    chute = int(chute_str)
    
    if (chute < 1 or chute > 100):
        print ("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou o número e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print ("Você errou! Seu chute foi maior que o número.")
        elif(menor):
            print ("Você errou! Seu chute foi menor que o número.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print("Fim do jogo")