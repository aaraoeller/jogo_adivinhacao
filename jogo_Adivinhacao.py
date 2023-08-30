import random

def chute_computador(x):
    baixo = 1
    alto = x
    dica = ''
    while dica != 'c':
        if baixo != alto:
            chute = random.randint(baixo, alto)
        else:
            chute = baixo 
        dica = input(f' O seu número é {chute} ? Muito alto (H), muito baixo (L), ou correto (C)? ').lower()
        if dica == 'h':
            alto = chute - 1
        elif dica == 'l':
            baixo = chute + 1
    
    print(f'Eu acertei!')

chute_computador(1000)