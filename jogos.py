
import subprocess
import sys
try:
    import colorama
except ImportError:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    except subprocess.CalledProcessError:
        print("Não foi possível instalar o módulo colorama")
from colorama import Fore, Style
import time

import adivinhacao
import forca

def escolha_jogo():
    while True:
        print(Fore.LIGHTBLUE_EX + '********************************')
        print('********************************')
        print("ESCOLHA O SEU JOGO \n ")
        print('********************************')
        print('******************************** \n' + Style.RESET_ALL )

        print(Fore.YELLOW + "(1) ADIVINHAÇÃO  (2) JOGO DA FORCA (3) JOGO DA VELHA ou (4) para SAIR \n" + Style.RESET_ALL)

        jogo = input("QUAL JOGO? ")

        if jogo == "1" or jogo.lower() == "adivinhação":
            print("Jogando adivinhacao")
            adivinhacao.jogar()
            break
        elif jogo == "2" or jogo.lower() == "jogo da forca":
            print("Jogando jogo da forca")
            forca.jogar()
            break
        elif jogo == "3" or jogo.lower() == "jogo da velha":
            print("Jogando jogo da velha")
            import jogo_da_velha
            jogo_da_velha
            break
        elif jogo.lower() == "sair" or jogo == "4":
            print("Saindo do jogo")
            sys.exit(0)
        else:
            print(Fore.RED + " \n OPÇÃO INVÁLIDA! aguarde e tente novamente \n " + Style.RESET_ALL)
            time.sleep(2)  # Pausa por 2 segundos antes de repetir o laço
if(__name__ == "__main__"):
 escolha_jogo()