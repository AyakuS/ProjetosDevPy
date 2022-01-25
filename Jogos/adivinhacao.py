import random
import Jogos

def jogar():

    print("=================================")
    print("Bem vindo ao jogo de adivinhação!")
    print("=================================")

    num_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Escolha o nivel de dificuldade sendo: [1] Fácil, [2] Médio e [3] Difícil")
    nivel = int(input("Defina o nivel: "))

    if (nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute_str = input("Digite um numero do 1 a 100: ")
        print("Você digitou: ",chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print(f"Você precisa digitar um numero de 1 a 100 ! Perdeu {rodada} tentativa")
            continue

        if (chute == num_secreto):
            print(f"Você acertou e fez {pontos} pontos ")
            print("Fim do jogo!")
            break
        else:

            pontos_perdidos = abs(num_secreto - chute) // 3
            pontos = pontos - pontos_perdidos

            if(chute > num_secreto):
                print("Você digitou um numero maior ! Tente um outro menor !.")
                if(rodada == tentativas):
                    print(f'O numero secreto era {num_secreto}. Você fez um total {pontos} pontos')
                    print("Fim do jogo!")
            elif (chute < num_secreto):
                print("Você digitou um numero menor ! Tente um outro maior! ")
                if (rodada == tentativas):
                    print(f'O numero secreto era {num_secreto}. Você fez um total {pontos} pontos')
                    print("Fim do jogo!")
    Jogos.jogar_novamente()

if (__name__ == "__main__"):
    jogar()