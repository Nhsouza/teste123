import random

numero_aleatorio = random.randint(1,10000)


tentativa = 0
while tentativa < 10:
  print(f'Você tem {10- tentativa} tentativas ')
  chute = int(input('Digite um numero de 1 a 10000: '))

  if chute == numero_aleatorio:
    print('Parabéns você acertou o número')
    break
  elif chute < numero_aleatorio:
    print('O número é Maior ')
    tentativa = tentativa+1

  elif chute > numero_aleatorio:
    print('O número é Menor ')
    tentativa = tentativa+1
else:
  print(f'Você perdeu =/ Acabaram as tentativas. O número era {numero_aleatorio}')
