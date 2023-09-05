import random

print('========== INICIANDO O JOGO ==========')

def chute_computador(x):
    baixo = 1
    alto = x
    dica = ''
    chances = 10
    tentativas = 0


    escolha = input(f'Escolha um número entre 1 e {x}. O número que você escolheu é par (P) ou ímpar (I)? ').lower()

    while dica != 'c' and chances > 0:
        if baixo <= alto:
            chute = random.randint(baixo, alto)
        else:
            print(f'Intervalo inválido: baixo ({baixo}) é maior que alto ({alto}).')
            break

        if (escolha == 'p' and chute % 2 == 0) or (escolha == 'i' and chute % 2 != 0):
            print("Computador: ok, entendi...")
        
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