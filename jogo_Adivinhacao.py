import random

def chute_computador(x):
    baixo = 1
    alto = x
    dica = ''
    while dica != 'c':
        if baixo <= alto:
            chute = random.randint(baixo, alto)
        else:
            chute = baixo
            break
        dica = input(f' O seu número é {chute} ? Muito alto (H), muito baixo (L), ou correto (C)? ').lower()
        if dica == 'h':
            if chute < alto:
                alto = chute - 1
            else:
                baixo = chute + 1
        elif dica == 'l':
            baixo = chute + 1
    print(f'Eu já sabia, só estava te testando!')

chute_computador(10)