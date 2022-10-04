while True:
    digitado = input('Digite algo: ')
    print('O tipo primitivo desse valor é', type(digitado))
    print(f'Só tem espaços? {digitado.isspace()}')
    print(f'É um número? {digitado.isnumeric()}')
    print(f'É alfabético? {digitado.isalpha()}')
    print(f'É alfanumérico? {digitado.isalnum()}')
    print(f'Está em maiúsculas? {digitado.isupper()}')
    print(f'Está em minúsculas? {digitado.islower()}')
    print(f'Está capitalizada? {digitado.istitle()}')
    """
    if digitado.isalpha():
        print('O valor digitado é Alfabético')
    elif digitado.isnumeric():
        print('O valor digitado é Númerico')
    elif digitado.isalnum():
        print('O valor digitado é Alfabético e Númerico')
    elif digitado.isspace():
        print('O valor digitado é Espaço')
    else:
        print('Nenhuma das opções')"""
