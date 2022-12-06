import re
from operacoes import *
expressao = "2+3*5/2**2+55-78/13"

exp = "2 + 3 * 5/2 ** 2 + 55 - 78 / 13"
exp = exp.strip().replace(' ', '')
print(exp)

def getNumeros(expressao, operador):
    expressao_operador = re.compile('{}'.format(operador))
    indice = re.search(expressao_operador, expressao)
    if indice != None:
        num1 = expressao[indice.start()-1]
        num2 = expressao[indice.end()]
        return indice, num1, num2,
    else:
        return None, None, None,

num1 = 0
num2 = 0

while(True):
    indice, num1, num2 = (getNumeros(expressao, '\/'))
    if indice == None:
        print('----')
        break
    resultado = divisao(num1, num2)
    expressao = expressao.replace(expressao[indice.start()-1:indice.end()+1], str(resultado))
    print(num1, num2)
    print(expressao)
    

while(True):
    indice, num1, num2 = (getNumeros(expressao, '\*{2}'))
    if indice == None:
        print('----')
        break
    resultado = exponenciacao(num1, num2)
    expressao = expressao.replace(expressao[indice.start()-1:indice.end()+1], str(resultado))
    print(num1, num2)
    print(expressao)

while(True):
    indice, num1, num2 = (getNumeros(expressao, '\*'))
    if indice == None:
        print('----')
        break
    resultado = multiplicacao(num1, num2)
    expressao = expressao.replace(expressao[indice.start()-1:indice.end()+1], str(resultado))
    print(num1, num2)
    print(expressao)
