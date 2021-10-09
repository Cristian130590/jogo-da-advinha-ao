#programa que vai pensar um numero de 0 a 10 mostrando quantos palpites foram neessarios para acertar

from random import randint
computador = randint(0, 10)
print(' sou seu computador ...tente advinhar o numero que estou pensando de 0 a 10:')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input(' qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(' mais...tente de novo')
        elif jogador > computador:
            print(' menos... tente de novo')
print(' voçe acertou com {} palpites. parabens.'.format(palpites))




