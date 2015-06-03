#arquivos

import sys

acao = input('Ação a fazer [1-escrever | 2-ler]')

if (acao == '1'):
    temp = open('temp.txt','w')
    for i in range(100):
        temp.write('%03d\n' % i)
    temp.close()
elif (acao == '2'):
    print('Opção 2')
    temp = open('temp.txt','r')
    for x in temp:
        sys.stdout.write(x);
    temp.close()
else:
    print('Escolha 1 ou 2')


