import random

def guess(x):
    random_number = random.randint(1,x)
    chute = 0
    while chute != random_number:
        chute = int(input(f'chute um número entre 1 e {x}: '))
        if chute < random_number:
            print('Desculpe, chute novamente. Muito baixo.')
        elif chute > random_number:
            print('Desculpe, chute novamente. Muito alto.')
    
    print(f'Eu acertei!')

def chute_computador(x):
    baixo = 1
    alto = x
    dica = ''
    while dica != 'c':
        if baixo != alto:
            chute = random.randint(baixo, alto)
        else:
            chute = baixo 
            dica = input(f'{chute} é Muito alto (H), muito baixo (L), ou correto (C)? ')
        if dica == 'h':
            alto == chute - 1
        elif dica == 'l':
            baixo = chute + 1
    
    print(f'Eu acertei!')

chute_computador(100)