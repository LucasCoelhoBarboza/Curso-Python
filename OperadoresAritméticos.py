#   OPERADORES

#  + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão
#_______________________________________________________
#   ORDEM DE PRECEDÊNCIA

# 1º ()
# 2º **
# 3º * / // %
# 4º + - 
#_______________________________________________________

n= int(input('digite um némero: '))
print('analisando o valor {}, seu antecesor é {} e seu sucessor é {}'.format(n, (n-1), (n+1)))