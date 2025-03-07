import random 
print('-=-'*10)
print('vamos fazer um jogo de adivinhação, escolha um numero de 1 a 10')
n1 = int(input('jogador 1: '))
n2 = int(input('jogador 2: '))
n3 = random.randint(1,10)
if n1 == n3:
print('jogador 1 ganhou')
elif n2 == n3:
print('jogador 2 ganhou')
else:
print('muito burro, o numero era {}'.format(n3))