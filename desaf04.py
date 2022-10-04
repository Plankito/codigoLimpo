def verificacao(digitado):
        if digitado:
            return "Verdadeiro!"
        else:
            return "Falso!"
while True:
    digitado = input('\nDigite algo: ')
    print('\n-----------------------------------')
    print(f'O tipo primitivo de ({digitado}) é', type(digitado))
    print('-----------------------------------')
    print(f'Só tem espaços? {verificacao(digitado.isspace())}')
    print(f'É um número? {verificacao(digitado.isnumeric())}')
    print(f'É alfabético? {verificacao(digitado.isalpha())}')
    print(f'É alfanumérico? {verificacao(digitado.isalnum())}')
    print(f'Está em maiúsculas? {verificacao(digitado.isupper())}')
    print(f'Está em minúsculas? {verificacao(digitado.islower())}')
    print(f'Está capitalizada? {verificacao(digitado.istitle())}')
    print('-----------------------------------\n')
    



