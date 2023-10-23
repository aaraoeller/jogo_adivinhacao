import random

def chute_computador():
    baixo = 0
    alto = 100
    dica = ''

    chute = random.randint(baixo, alto)

    while dica != 'c':

        dica = input(f'O seu número é {chute}? Muito alto (H), Muito baixo (L), ou correto (C)?').lower()

        if dica == 'h':
            alto = chute
        elif dica == 'l':
            baixo = chute

        chute = random.randint(baixo, alto)

    if dica == 'c':
        print(f'Eu adivinhei, o seu número é {chute}')
    else:
        print('Minhas chances se esgotaram')

chute_computador()