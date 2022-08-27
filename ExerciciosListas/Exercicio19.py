"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e
informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
sistema = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
opcao = [0] * 6
while True:
    print("Sistemas Operacionais:")
    print('1 - Windows Server\n'
          '2 - Unix\n'
          '3 - Linux\n'
          '4 - Netware\n'
          '5 - Mac OS\n'
          '6 - Outro')
    while True:
        voto = int(input('Digite seu voto: '))
        if voto > 6 or voto < 0:
            print('Opção inválida.')
        else:
            break
    if voto == 0:
        break
    opcao[voto -1] = opcao[voto -1] + 1

print('Sistema Operacional     Votos  %')
print('----------------------------------')
cont = 0
melhor = 0
melhorSis = ''
perc = 0
for s in opcao:
    print('%s   %d   %.2f%%' % (sistema[cont], s,(s * 100) / sum(opcao) ))
    if s > melhor:
        melhor = s
        melhorSis = sistema[cont]
        perc = (s * 100) / sum(opcao)
    cont += 1

print('----------------------------------')
print('Total   %d' % sum(opcao))
print('O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos.' % (melhorSis, melhor, perc))
