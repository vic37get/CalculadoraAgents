import re

from operacoes import *


def buscaParenteses(expressao):
    abertura_parenteses = []
    fechamento_parenteses = []
    for index, caractere in enumerate(expressao):
        if caractere == '(':
            abertura_parenteses.append(index)
        if caractere == ')':
            fechamento_parenteses.append(index)
    try:
        inicio = max(abertura_parenteses)
        fim = min(fechamento_parenteses)
        return expressao[inicio:fim+1]
    except ValueError:
        return None

def identificaNumerais(expressao, indice_caractere):
    OPERACOES = re.compile('(((raiz)|([\^*\/+\-\(\)])))')
    INICIO = ''
    FIM = ''

    for caractere in range(indice_caractere-1, 0, -1):      
        if re.search(OPERACOES, expressao[caractere]) == None:
            INICIO = str(expressao[caractere]) + INICIO
        else:
            break

    for caractere in range(indice_caractere+1, len(expressao)):
        if re.search(OPERACOES, expressao[caractere]) == None:
            FIM += str(expressao[caractere])
        else:
            break

    #print(int(INICIO), int(FIM))
    return int(INICIO), int(FIM)
        
def identificaOperacao(expressao):
    for indice, caractere in enumerate(expressao):
        #print(caractere)
        if caractere == '^':
            #print(expressao)
            INICIO, FIM = identificaNumerais(expressao, indice)
            resultado = exponenciacao(INICIO, FIM)
            #print('INICIO: ', INICIO, 'FIM: ', FIM, 'RESULTADO: ',resultado)
            return '{}{}{}'.format(INICIO, caractere, FIM), resultado

        elif caractere == 'raiz':
            ...
        elif caractere == '*':
            ...
        elif caractere == '/':
            ...
        elif caractere == '+':
            ...
        elif caractere == '-':
            ...
    return None

def removeParenteses(busca, expressao):
    OPERACOES = re.compile('(((raiz)|([\^*\/+\-])))')
    PARENTESES = re.compile('[\)\()]')
    if re.search(OPERACOES, busca) == None:
        expressao[busca.start():busca.end()] = re.sub(PARENTESES, '', expressao)
    return expressao
            
def Master(expressao):
    busca = ''
    while busca != None:
        busca = buscaParenteses(expressao)
        if busca != None:
            #print(expressao)
            EXPRESSAO_RESOLVIDA, RESULTADO = identificaOperacao(busca)
            #print('EXPRESSAO RESOLVIDA: ',EXPRESSAO_RESOLVIDA)
            expressao = expressao.replace(EXPRESSAO_RESOLVIDA, str(RESULTADO))
            
            print(expressao)
    print('fim')


entrada = "23 + 12 - 55 + 2 + 4 - 8 / ((2^2)^2)"
entrada = entrada.replace(' ', '')
Master(entrada)


##TRABALHAR COM INDICES É MELHOR

