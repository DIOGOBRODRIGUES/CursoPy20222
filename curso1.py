#ex1 
#nome = input('Qual o seu nome?')
#print('Seja bem vindo ' + nome )

#ex2
#dia = input ('Qual o dia?')
#mes = input ('Qual o mês?')
#ano = input ('Qual o ano de nascimento?')
#print('Você nasceu no dia ' + dia + 'de ' + mes + 'de ' +ano ) 

#ex3
#num1 = int(input('Digite o primeiro número: '))
#num2 = int(input('Outro número: '))
#soma = num1 + num2
#print('a soma dos dois números é ', soma)

#ex4
##n1 = input('n1: ')
##n2 = input('n2: ')
##operacao = input('Digite a operação: ')
##
##resultado = None
##
##if operacao == '+':
##    resultado = float(n1) + float(n2)
##    print('{} + {} = {}'.format(n1, n2, resultado))
##if operacao == '

#ex5
##for c in range(1, 6):
##    print('oi ', c)
##
##for c in range(1, 6, 2):
##    print('oi ', c)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #s = s + n

print('O somatório de todos os valores foi {}'.format(s))
