print('==== sistema====')

nome= input('digite seu nome completo:')
print('nome:',nome)

rgm= input('digite seu rgm:')
print('rgm:', rgm)

data= input('digite sua data de nascimento:')
print('data de nascimento:', data )


n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))

op = input('digite a operação (adição, subtração, multiplicação, divisão):').lower()

if op == 'adição':
    resultado = n1+n2
    simbolo = '+'
elif op == 'subtração':
     resultado = n1-n2
     simbolo = '-'
elif op == 'multiplicação':
     resultado = n1 * n2
     simbolo = '*'
elif op == 'divisão':
     if n2 !=0:
        resultado = n1 / n2
        simbolo = '/'
     else:
         resultado = 'não é possível dividir por zero'
         simbolo = '/'
else:
    resultado = 'operação inválida'
    simbolo = '?'


print('\n=== RESULTADO FINAL ===')
print('nome:' , nome)
print('rgm:', rgm)
print('data:', data)
print('operação:', op)
print(f'{n1}{simbolo}{n2}={resultado}')
