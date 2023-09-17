import random
from colorama import Fore, Style
import  jogos

MIN_RANGE = 1
MAX_RANGE = 100
DIFICULDADES = {
    1: (30, 1, 30),
    2: (20, 1, 40),
    3: (10, 1, 50),
    4: (5, 1, 60),
    5: (3, 1, 70)
}
pontuacao_alta = 0

def jogar():

    def escolher_dificuldade():
        nivel = 0
        while nivel not in DIFICULDADES:
            print(Fore.BLUE + "(1) MUITO FÁCIL (2) FÁCILO (3) MÉDIO (4) DIFÍCIL (5) MUITO DIFÍCIL \n" + Style.RESET_ALL)
            nivel = int(input("Escolha um nível de dificuldade (1 a 5): "))
            if nivel not in DIFICULDADES:
                print(Fore.RED + " \n Nível de dificuldade inválido. Escolha entre 1 e 5. \n" + Style.RESET_ALL)
        return nivel

    def dica_rodada(rodada, numero_secreto, nivel):
        dicas = ["", "O número secreto é par!", "O número secreto é menor do que a metade.", "O número secreto é divisível por três!"]
        if rodada == len(DIFICULDADES[nivel]) // 2:
            if numero_secreto % 2 == 0:
                return dicas[1]
        elif rodada == len(DIFICULDADES[nivel]) // 3:
            if numero_secreto < numero_secreto // 2:
                return dicas[2]
        elif rodada == len(DIFICULDADES[nivel]) // 4:
            if numero_secreto % 3 == 0:
                return dicas[3]
        return dicas[0]

    def jogo_adivinhacao():
        global pontuacao_alta
        jogar_novamente = 's'
        while jogar_novamente == 's':
            print(Fore.GREEN + '********************************')
            print('********************************')
            print("Bem vindo ao jogo de Adivinhação \n ")
            print("Você receberá 10 pontos a cada ACERTO, e -1 ponto a cada ERRO \n")
            print(f"A pontuação mais alta até agora é {pontuacao_alta} \n")
            print('********************************')
            print('******************************** \n' + Style.RESET_ALL)


            nivel = escolher_dificuldade()
            total_tentativas, minimo, maximo = DIFICULDADES[nivel]
            numero_secreto = random.randint(minimo, maximo)
            pontos = total_tentativas * 10



            for rodada in range(1, total_tentativas + 1):
                print(f"\n Tentativa {rodada} de {total_tentativas} \n")
                chute = int(input(f" Digite um número entre {minimo} e {maximo}: "))

                if chute < minimo or chute > maximo:
                    print(Fore.RED + f"Você deve digitar um número entre {minimo} e {maximo}! \n" + Style.RESET_ALL)
                    continue

                acertou = numero_secreto == chute

                if acertou:
                    print(Fore.GREEN + f"VOCÊ ACERTOU! Sua pontuação final é {pontos} \n" + Style.RESET_ALL)
                    if pontos > pontuacao_alta:
                        print(Fore.YELLOW + "Parabéns! Você bateu o recorde de pontuação alta!" + Style.RESET_ALL)
                        pontuacao_alta = pontos
                    break
                else:
                    pontos -= abs(numero_secreto - chute)
                    if chute > numero_secreto:
                        print(Fore.RED + "VOCÊ ERROU! O seu chute foi maior do que o número secreto \n" + Style.RESET_ALL)
                        maximo = chute - 1
                    else:
                        print(Fore.RED + "VOCÊ ERROU! O seu chute foi menor do que o número secreto \n" + Style.RESET_ALL)
                        minimo = chute + 1

                    dica = dica_rodada(rodada, numero_secreto, nivel)
                    if dica:
                        print(Fore.YELLOW + dica + Style.RESET_ALL)

            print('********************************')
            print("Fim do jogo")

            if chute != numero_secreto:
                print("\n","O NÚMERO SECRETO É:", numero_secreto, "\n", f"Total de pontos: {pontos}")

            jogar_novamente = input('\nDeseja jogar novamente? (s/n): ').lower()
            while jogar_novamente not in ['s', 'n']:
                jogar_novamente = input(Fore.RED + 'Resposta inválida! Deseja jogar novamente? (s/n): ' + Style.RESET_ALL).lower()

            if jogar_novamente == 's':
                continue
            else:
                print('\n********************************')
                print(Fore.YELLOW + "Obrigado por jogar!" + Style.RESET_ALL)
                print('********************************\n')

                while True:
                    menu_jogos = input("Deseja retornar ao" + Fore.BLUE + " MENU DE JOGOS?" + Style.RESET_ALL + " (s/n): ")
                    if menu_jogos.lower() == "s":
                        jogos.escolha_jogo()
                        break
                    elif menu_jogos.lower() == "n":
                        print('\n******************************** ')
                        print(Fore.YELLOW + "Obrigado por jogar!" + Style.RESET_ALL)
                        print('********************************\n')
                        break
                    else:
                        print(Fore.RED + "\n OPÇÃO INVÁLIDA! tente novamente \n" + Style.RESET_ALL)


        print('\n ********************************')
        print('******************************** \n')


    jogo_adivinhacao()
if(__name__ == "__main__"):
 jogar()