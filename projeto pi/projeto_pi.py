import os
import platform
import time


def clear():
  sys = platform.system()
  cls = None

  if (sys == 'Windows'):
    cls = lambda: os.system('cls')
  elif (sys == 'Linux'):
    cls = lambda: os.system('clear')

  if (cls != None): cls()



def error(msg):
  for i in range(1, 4):
    clear()
    print(msg + ('.' * i))
    time.sleep(1)

  clear()


def converter(num, base):
  resultado = list()
  exa = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

  while num > 0:
    resultado.append(num % base)
    num //= base

  resultado = list(reversed(resultado))

  for i, alg in enumerate(resultado):
   
    resultado[i] = str(exa.get(alg) if alg > 9 else alg)

  return ''.join(map(str, resultado))


while True:
  clear()

  print('##### Conversor de números decimais para outras bases #####\n')
  print('[1] Converter Decimal para Binário')
  print('[2] Converter Decimal para Octal')
  print('[3] Converter Decimal para Hexadecimal\n')
  print('[0] Sair\n')

  try:
    opt = int(input('Escolha uma das opções para Conversão de Base: '))

    if opt == 0:
      clear()
      break
    elif opt >= 1 and opt <= 3:
      num = int(input('Digite um número decimal para Conversão: '))

      if opt == 1:
        print(f'O valor {num} convertido para BINÁRIO é {converter(num,2)}.')
      elif opt == 2:
        print(f'O valor {num} convertido para OCTAL é {converter(num,8)}.')
      elif opt == 3:
        print(f'O valor {num} convertido para HEXADECIMAL é {converter(num,16)}.')
      else:
        error('Opção inválida')

      input('\nPressione Enter retornar.')
    else:
      error('Opção Inválida')
  except:
    error('Valor inválido')
