#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero_i_p = int(input('Digite um numero:\n'))
if numero_i_p % 2 == 0:
    print('\nNumero é par.')
else:
    print('\nO numero é impa.')


#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade_p = int(input('Qual a sua idade?\n'))
if 0 < idade_p <= 12:
    print('Criança')
elif 12 < idade_p < 18:
    print('Adolescente')
elif idade_p > 18:
    print('Adulto')
else:
    print('valor invalido')

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario_mateus = 'mateusramos'
senha_mateus = 'mateus123'

usuairo = input('usuario:\n')
senha = input('senha:\n')

if usuairo == usuario_mateus and senha == senha_mateus:
    print('login bem sucedido!')
else:
    print("Credenciais inválidas. Tente novamente.")

