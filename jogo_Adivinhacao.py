import random

print('========== INICIANDO O JOGO ==========')

def chute_computador(x):
    baixo = 1
    alto = x
    dica = ''
    chances = 10
    tentativas = 0

    # Pedir ao jogador para escolher entre par (P) ou ímpar (I)
    escolha = input(f'Escolha um número entre 1 e {x}. O número que você escolheu é par (P) ou ímpar (I)? ').lower()

    while dica != 'c' and chances > 0:
        # Gerar um chute que corresponda à escolha do jogador
        if escolha == 'p':
            chute = random.randint(baixo, alto)
            while chute % 2 != 0:
                chute = random.randint(baixo, alto)
        elif escolha == 'i':
            chute = random.randint(baixo, alto)
            while chute % 2 == 0:
                chute = random.randint(baixo, alto)
        
        print(f'Computador: Eu tenho {chances} chances.')

        dica = input(f'O seu número é {chute} ? Muito alto (H), muito baixo (L), ou correto (C)? ').lower()
        if dica == 'h':
            alto = chute - 1
        elif dica == 'l':
            baixo = chute + 1
        chances -= 1
        tentativas += 1

    if dica == 'c':
        print(f'Computador: Eu adivinhei, o seu número é ({chute})')
        print(f'Computador: Foram necessárias {tentativas} tentativas para acertar.')
    else:
        print(f'Computador: As minhas chances se esgotaram. Mas eu acho que o número era {x}.')

chute_computador(100)