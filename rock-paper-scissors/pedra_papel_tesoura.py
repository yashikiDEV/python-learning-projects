import random

TESOURA = "3"
PEDRA = "1"
PAPEL = "2"


def resultado(jogador, computador):
    escolhas_validas = {TESOURA, PEDRA, PAPEL}

    if jogador not in escolhas_validas:
        return 'Jogada inválida'

    if jogador == computador:
        return 'Empate'

    if (
        (jogador == TESOURA and computador == PAPEL)
        or (jogador == PEDRA and computador == TESOURA)
        or (jogador == PAPEL and computador == PEDRA)
    ):
        return 'Jogador vence'

    if (
        (jogador == TESOURA and computador == PEDRA)
        or (jogador == PEDRA and computador == PAPEL)
        or (jogador == PAPEL and computador == TESOURA)
    ):
        return 'Computador vence'

    return 'Jogada inválida'


if __name__ == "__main__":
    while True:
        print("Escolha uma opção:")
        print()
        print("1 - pedra\n")
        print("2 - papel\n")
        print("3 - tesoura\n")
        print("Digite 'sair' para encerrar o jogo.\n")

        jogador = input("Digite o número correspondente à sua jogada: ")

        if jogador == "sair":
            print("Encerrando o jogo...")
            break

        computador = str(random.randint(1, 3))
        print(f"Jogada do computador: {computador}")
        print("resultado:" + resultado(jogador, computador))