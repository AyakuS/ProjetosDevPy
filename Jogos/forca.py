import Jogos
import random


def abertura_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = [linha.strip() for linha in arquivo]

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["*" for _ in palavra]


def dificuldade():
    while True:
        print("Escolha o nivel de dificuldade: [1]- Fácil, [2]-Médio e [3]-Dificil")
        nivel = int(input("Dificuldade: "))
        if nivel == 1:
            print("Dificuldade [1]- Fácil, você possui 6 tentativas")
            return 7

        elif nivel == 2:
            print(" Dificuldade [2]-Médio, você possui 3 tentativas")
            return 3

        elif nivel == 3:
            print("Dificuldade [3]-Dificil, você possui 2 tentativas")
            return 2

        else:
            print("Digite um valor de dificuldade valido! ")


def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def jogar():
    abertura_jogo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = dificuldade()

    while not acertou and not enforcou:
        nova_palavra = ""
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == tentativas
        acertou = "*" not in letras_acertadas

        print(f"Você utilizou um total de {erros}, das suas {tentativas} tentativas!")
        for letra in letras_acertadas:
            nova_palavra += letra
        print(nova_palavra)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

    print("Fim do jogo")

    Jogos.jogar_novamente()


if __name__ == "__main__":
    jogar()
