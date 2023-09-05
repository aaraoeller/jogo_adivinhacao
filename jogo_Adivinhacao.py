import random
import time

print('========== INICIANDO O JOGO ==========')

def chute_computador():
    baixo = -100
    alto = 100
    dica = ''
    chances = 10
    tentativas = 0
    inicio = time.time()


    escolha = input(f'Escolha um número entre {baixo} e {alto}. O número que você escolheu é par (P) ou ímpar (I)? ').lower()

    while dica != 'c' and chances > 0:

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

    fim = time.time()
    tempo_total = fim - inicio

    if dica == 'c':
        print(f'Computador: Eu adivinhei, o seu número é ({chute})')
        print(f'Computador: Foram necessárias {tentativas} tentativas para acertar.')
        print(f'Computador: Tempo total de jogo: {tempo_total:.2f} segundos')
    else:
        print(f'Computador: As minhas chances se esgotaram.')

chute_computador()