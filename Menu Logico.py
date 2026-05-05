# Proposta  --> Desenvolvimento de programas para resolver problemas matemáticos básicos (soma, 
#               subtração, multiplicação, divisão, cálculo de média, equação de segundo grau, fatorial, 
#               conversão de unidades, tabuada, Fibonacci). Utilizar um menu de opções para escolher a 
#               operação a ser realizada.

import math
from colorama import Fore, Style, init
init()

print(Fore.BLUE + "\n--RESOLUÇÃO DE CONTAS MATEMÁTICAS--\n" + Style.RESET_ALL)

# Menu para navegação 
while True:
    print(Fore.GREEN + "\n============= MENU =============")
    print("0  - Sair do menu")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Cáculo de Média")
    print("6 - Equação de Segundo Grau")
    print("7 - Fatorial")
    print("8 - Conversão de Unidades")
    print("9 - Tabuada Completa")
    print("10 - Fibonanacci")
    print("=================================\n")
    print(Style.RESET_ALL)
# Fore.GREEN serve para definir a cor para verde, já o Style.RESET_ALL serve para delimitar onde a cor escolhida termina

    opcao = input("- ESCOLHA A OPÇÃO DESEJADA DO MENU: ")
    print("\n")

    if opcao == "1":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Soma ||" + Style.RESET_ALL)
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        conta = a + b
        print(f"\nO Resultado da soma é: {conta:.2f}")

    elif opcao == "2":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Subtração ||" + Style.RESET_ALL)
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        conta = a - b
        print(f"\nO Resultado da subtração é: {conta:.2f}")

    elif opcao == "3":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Multiplicação ||" + Style.RESET_ALL)
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        conta = a * b
        print(f"\nO Resultado da multiplação é: {conta:.2f}")

    elif opcao == "4":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Divisão ||" + Style.RESET_ALL)
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        if b != 0:
            conta = a / b
            print(f"\nO resultado da divisão é: {conta:.2f}")
        else:
            print("\nNão é possível dividir por zero !!!")

    elif opcao == "5":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Média ||" + Style.RESET_ALL)
        quantidade = int(input("Digite quantos números deseja inserir no cálculo --> "))
        soma = 0 

        for i in range(quantidade):
            # A linha 62 serve para o úsuario colocar quantos números tem no seu cálculo de média
            # Ao colocar esse número o sistema vai pedir separadamente cada valor e realizar a conta

            numero = float(input(f"Digite o número {i+1}: ")) 
            # A função {i+1} serve para começar a contagem no 1 e ignorar o zero, facilitando a representação

            soma = (soma + numero)

        media = soma / quantidade
        print(f"\nO resultado do cálculo da média é: {media:.2f}")

    elif opcao == "6":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Equação de Segundo Grau ||" + Style.RESET_ALL)
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        delta = ((b**2) - (4*a*c))

        # A igual a zero
        if a == 0:
            print("\nNão é equação do segundo grau!!!\n")

        # Delta negativo
        elif delta < 0:
            print("\nNão há raízes reais!!!\n")

        # Delta igual a zero
        elif delta == 0:
            x = -b / (2*a)
            print(f"\nRaiz única: x = {x:.2f}\n")

        # Delta positivo
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)

            print(f"\nx1 = {x1:.2f}")
            print(f"x2 = {x2:.2f}\n")

    elif opcao == "7":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo Fatorial ||" + Style.RESET_ALL)
        num = int(input("Digite um número: "))
        fatorial = 1

        for i in range(1, num + 1):
            fatorial = fatorial * i

        print(f"\nO resultado da fatoração é: {fatorial:.2f}")

    elif opcao == "8":
        print(Fore.GREEN + "|| Você escolheu realizar um cálculo para Conversão de Unidades ||" + Style.RESET_ALL)

        # Sub-menu para escolher o tipo de conversão a ser realizada
        while True:
            print(Fore.MAGENTA + "\n========== MENU DE CONVERSÃO ===========")
            print("0 - Sair do Sub-menu")
            print("1 - Conversão de Km/h para M/s")
            print("2 - Conversão de Horas para Minutos")
            print("3 - Conversão de Kg para g")
            print("4 - Conversão de Celsius para Fahrenheit")
            print("====================================\n")
            print(Style.RESET_ALL)

            escolha = input("- ESCOLHA A OPÇÃO DESEJADA DO MENU: ")
            print("\n")

            if escolha == "1":
                print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Km/h para M/s ||" + Style.RESET_ALL)
                kmh = float(input("Digite a velociade (Km/h): "))
                ms = kmh / 3.6
                print(f"\nA conersão de {kmh:.2f} Quilometros por hora é {ms:.2f} Metros por segundo")

            elif escolha == "2":
                print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Horas para Minutos ||" + Style.RESET_ALL)
                horas = float(input("Digite as horas desejadas: "))
                min = horas * 60
                print(f"\nA conversão de {horas:.2f} Horas é {min:.2f} Minutos")

            elif escolha == "3":
                print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Kg para g ||" + Style.RESET_ALL)
                kg = float(input("Digite as Quilogramas: "))
                g = kg * 1000
                print(f"\nA conversão de {kg:.2f} Quilogramas é {g:.2f} gramas")

            elif escolha == "4":
                print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Celsius para Fahrenheit ||" + Style.RESET_ALL)
                c = float(input("Digite a Temperatura em celsius: "))
                f = (c * 9/5) + 32
                print(f"\nA conversão de {c:.2f} Graus Celsius é {f:.2f} Fahrenheit")

            elif escolha == "0":
                print(Fore.YELLOW + "|| VOCÊ ESCOLHEU VOLTAR AO MENU PRINCIPAL ||" + Style.RESET_ALL)
                break
                # Nesse caso Break está encerrando o loop do sub-menu e retornando ao menu principal
            else:
                print(Fore.RED + "OPÇÃO INVÁLIDA!!" + Style.RESET_ALL)
                break

    elif opcao == "9":
        print(Fore.GREEN + "|| Você escolheu realizar uma Tabuada Completa ||" + Style.RESET_ALL)
        num = int(input("Digite o número da tabuada desejada: "))
        print("\n") 

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    elif opcao == "10":
        print(Fore.GREEN + "|| Você escolheu cálcular a Sequência de Fibonanacci ||" + Style.RESET_ALL)
        # É uma sucessão numérica infinita onde cada número é a soma dos dois anteriores, começando geralmente por 0 e 1

        x = int(input("Digite quantos termos deseja ver: "))
        a = 0
        b = 1
        
        for i in range(x):
            print(a)
            a, b = b, a + b
            # A função print veio primeiro para manter a sequência correta sem pular o zero

    elif opcao == "0":
        print(Fore.YELLOW + "|| VOCÊ ESCOLHEU FECHAR O MENU ||" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "OPÇÃO INVÁLIDA!!\n" + Style.RESET_ALL)
        break 