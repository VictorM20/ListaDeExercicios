"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá,
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo:
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza;
a.necessita troca do cabo ou conector;
a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""
opcao = [0] * 4
print('Situação do mouse')
print('1 - Necessita de esfera\n'
      '2 - Necessita de limpeza\n'
      '3 - Necessita troca do cabo ou conector\n'
      '4 - Quebrado ou inutilizado\n'
      '0 - Para finalizar o programare imprimir o relátorio ')
while True:
    ident = int(input('Nº de identificação: '))
    if ident == 0:
        break
    situacao = int(input('Digite o número do problema: '))
    opcao[situacao - 1] = opcao[situacao - 1] + 1
total = sum(opcao)
print('Situação                        Quantidade              Percentual')
print('1- necessita da esfera                  %d              %.2f' % (opcao[0], (100 * opcao[0]) / total))
print('2- necessita de limpeza                 %d              %.2f' % (opcao[1], (100 * opcao[1]) / total))
print('3- necessita troca do cabo ou conector  %d              %.2f' % (opcao[2], (100 * opcao[2]) / total))
print('4- quebrado ou inutilizado              %d              %.2f' % (opcao[3], (100 * opcao[3]) / total))
