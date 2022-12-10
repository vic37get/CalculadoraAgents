def divisao(num1, num2):
    return float(num1)/float(num2)

def adicao(num1, num2):
    return float(num1)+float(num2)

def subtracao(num1, num2):
    return float(num1)-float(num2)

def multiplicacao(num1, num2):
    return float(num1)*float(num2)

def exponenciacao(num1, num2):
    try:
        resultado = int(num1)**int(num2)
    except ValueError:
        resultado = float(num1)**float(num2)
    return resultado

def raiz(num1):
    return float(num1)**1/2