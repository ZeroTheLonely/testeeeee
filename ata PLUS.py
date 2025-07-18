import random

def jogar():
    numero_secreto = random.randint(1, 500)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 500.")
    print("Você tem 10 tentativas.")
    print("A qualquer momento, digite 'desistir' para encerrar o jogo.")

    while tentativas < max_tentativas:
        entrada = input(f"Tentativa {tentativas+1}/{max_tentativas} - Digite seu palpite ou 'desistir': ").strip().lower()
        if entrada == 'desistir':
            print(f"Você desistiu! O número secreto era {numero_secreto}.")
            return 0
        try:
            chute = int(entrada)
        except ValueError:
            print("Por favor, digite um número válido ou 'desistir'.")
            continue

        tentativas += 1

        if chute < numero_secreto:
            print("Errado! O número secreto é maior que", chute)
        elif chute > numero_secreto:
            print("Errado! O número secreto é menor que", chute)
        else:
            pontos = max(0, 11 - tentativas)  # 10 pontos se acertar na 1ª, 9 na 2ª, ..., 1 na 10ª
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas e ganhou {pontos} pontos.")
            return pontos
    print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")
    return 0

pontos_acumulados = 0
jogos_realizados = 0

while True:
    pontos = jogar()
    pontos_acumulados += pontos
    jogos_realizados += 1
    print(f"Pontos acumulados: {pontos_acumulados}")
    if jogos_realizados == 6:
        print("Você completou 6 jogatinas. Os pontos serão zerados!")
        pontos_acumulados = 0
        jogos_realizados = 0
    resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if resposta != 's':
        print("Obrigado por jogar! Até a próxima.")
        break