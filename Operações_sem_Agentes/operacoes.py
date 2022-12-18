def divisao(num1, num2):
    print('Realizando a operação de divisão entre os números {} e {}'.format(num1, num2))
    try:
        resultado = int(num1)/int(num2)
    except ValueError:
        resultado = float(num1)/float(num2)
    print('Resultado da operação: {}'.format(resultado))
    return resultado

def adicao(num1, num2):
    print('Realizando a operação de soma entre os números {} e {}'.format(num1, num2))
    try:
        resultado = int(num1)+int(num2)
    except ValueError:
        resultado = float(num1)+float(num2)
    print('Resultado da operação: {}'.format(resultado))
    return resultado

def subtracao(num1, num2):
    print('Realizando a operação de subtração entre os números {} e {}'.format(num1, num2))
    try:
        resultado = int(num1)-int(num2)
    except ValueError:
        resultado = float(num1)-float(num2)
    print('Resultado da operação: {}'.format(resultado))
    return resultado

def multiplicacao(num1, num2):
    print('Realizando a operação de multiplicação entre os números {} e {}'.format(num1, num2))
    try:
        resultado = int(num1)*int(num2)
    except ValueError:
        resultado = float(num1)*float(num2)
    print('Resultado da operação: {}'.format(resultado))
    return resultado

def exponenciacao(num1, num2):
    print('Realizando a operação de exponenciação entre os números {} e {}'.format(num1, num2))
    try:
        resultado = int(num1)**int(num2)
    except ValueError:
        resultado = float(num1)**float(num2)
    print('Resultado da operação: {}'.format(resultado))
    return resultado

def raiz(num1):
    #print('Realizando a operação de raiz entre os números {} e {} ({} ^ {})'.format(num1, num2))
    print('Realizando a operação de raiz quadrada do número {}'.format(num1))
    try:
        resultado = int(num1)**1/2
    except ValueError:
        resultado = float(num1)**1/2
    print('Resultado da operação: {}'.format(resultado))
    return resultado