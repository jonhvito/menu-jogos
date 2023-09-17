import time
import jogos
def jogar():
    print( '********************************')
    print('********************************')
    print("Bem vindo ao jogo da forca ")
    print('********************************')
    print('******************************** \n')

    palavra_secreta = "banana"

    print("fim de jogo")
    while True:
        jogar_novamente = input("Deseja retornar ao menu de jogos? (s/n) ")
        if jogar_novamente.lower() == "s":
            jogos.escolha_jogo()
            break
        elif jogar_novamente.lower() == "n":
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida, tente novamente")

if(__name__ == "__main__"):
 jogar()
