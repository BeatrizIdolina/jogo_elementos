import historia

def jogar():

    print(historia.inicio())
    print()

    print(historia.escolha_porta())
    print("1 - Porta Vermelha")
    print("2 - Porta Azul")

    porta = input("Escolha: ")

    if porta == "1":

        print()
        print(historia.sala_lava())
        print("1 - Herói do Fogo puxa a alavanca")
        print("2 - Heroína da Água tenta atravessar a lava")

        escolha = input("Escolha: ")

        if escolha == "1":

            print()
            print(historia.escadas())
            print("1 - Escada esquerda")
            print("2 - Escada direita")

            escada = input("Escolha: ")

            if escada == "1":

                print()
                print(historia.bau())
                print("1 - Abrir o baú")
                print("2 - Ignorar o baú")

                bau = input("Escolha: ")

                if bau == "1":
                    print()
                    print(historia.final_bom())
                else:
                    print()
                    print(historia.final_ruim("Vocês se perdem no templo."))

            else:
                print()
                print(historia.final_ruim("Vocês caem em uma armadilha."))

        else:
            print()
            print(historia.final_ruim("A Heroína da Água não consegue atravessar a lava."))

    elif porta == "2":

        print()
        print(historia.sala_agua())
        print("1 - Heroína da Água aperta o botão")
        print("2 - Herói do Fogo pula na água")

        escolha = input("Escolha: ")

        if escolha == "1":

            print()
            print(historia.ponte())
            print("1 - Atravessar a ponte")
            print("2 - Voltar")

            ponte = input("Escolha: ")

            if ponte == "1":
                print()
                print(historia.final_bom())
            else:
                print()
                print(historia.final_ruim("O templo fecha e a missão falha."))

        else:
            print()
            print(historia.final_ruim("O Herói do Fogo cai na água."))

    else:
        print("Escolha inválida.")


while True:

    jogar()

    print()
    resposta = input("Deseja jogar novamente? (sim/não): ")

    if resposta.lower() != "sim":
        print("Fim do jogo.")
        break