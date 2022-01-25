print("=================================")
print("Bem vindo ao jogo de adivinhação!")
print("=================================")

num_secreto = 42
tentativas = 3
rodada = 1

while rodada <= tentativas:
    print(f"Tentativa {rodada} de {tentativas}")
    chute_str = input("Digite um numero do 1 a 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print(f"Você precisa digitar um numero de 1 a 100 ! Perdeu {rodada} tentativa")

    if (chute == num_secreto):
        print("Você acertou, Mizerávi !! ")
        break
    elif (chute > num_secreto):
        print("Você digitou um numero maior ! Tente um outro menor !.")
    elif (chute < num_secreto):
        print("Você digitou um numero menor ! Tente um outro maior! ")

    rodada += 1