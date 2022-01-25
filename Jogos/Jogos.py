import forca
import adivinhacao

def jogar_novamente():
    print("Deseja jogar novamente: [s]-Sim e [n]-Não ")

    while True:
        desejo = input("Opção: ")
        if desejo == "s":
            return escolhe_jogo()
        elif desejo == "n":
            print("Jogo Finalizado !")
            break
        else:
            print("Valor digitado é invalido!")

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("Escolha o Jogo: [1] - Jogo da Forca e [2] - Jogo da Adivinhação ")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando da forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando da adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()