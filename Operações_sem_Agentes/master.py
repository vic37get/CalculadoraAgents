import re

from operacoes import *


#Função para buscar os parênteses em uma sentença.
def buscaParenteses(expressao):
    abertura_parenteses = []
    fechamento_parenteses = []
    for index, caractere in enumerate(expressao):
        if caractere == '(':
            abertura_parenteses.append(index)
        if caractere == ')':
            fechamento_parenteses.append(index)
    try:
        #Pegar o parêntese mais interno, para isso o inicial é o mais á direita (da lista de abertura de parenteses) e o final o mais á esquerda (da lista de fechamento de parenteses).
        inicio = max(abertura_parenteses)
        fim = min(fechamento_parenteses)
        #Se existem parenteses concorrentes. Exemplo: (2+5) - (5-7), o parentese de inicio vai ter indice maior que o de fim.
        if inicio > fim:
            for caractere in range(fim, 0, -1):
                if expressao[caractere] == '(':
                    inicio = caractere
                    return inicio, fim+1
        return inicio, fim+1 #Retorna o inicio e o fim da expressao com parênteses, incluindo os parênteses.
    except:
        return None, None

#Função para identificar os números envolvidos na operação, pegando a partir do indice do simbolo da operação
def identificaNumerais(expressao, indice_caractere):
    #regex para identificar operações matemáticas
    OPERACOES = re.compile('(((r)|([\^*\/+\-])))')
    #regex para identificar numeros, sejam inteiros ou decimais.
    adiciona_sinal = False

    PRIMEIRO_NUMERO = ''
    SEGUNDO_NUMERO = ''
    #Buscando o número que fica antes do sinal da operação, ou seja, o primeiro número da operação.
    for caractere in range(indice_caractere-1, -1, -1):
        if re.search(OPERACOES, expressao[caractere]) == None:
            if expressao[caractere] != '(':
                PRIMEIRO_NUMERO = str(expressao[caractere]) + PRIMEIRO_NUMERO
            else:
                continue
        else:
            if expressao[caractere] == '-':
                PRIMEIRO_NUMERO = str(expressao[caractere]) + PRIMEIRO_NUMERO
                adiciona_sinal = True
            break

    #Buscando o número que fica depois do sinal da operação, ou seja, o segundo número da operação.
    for caractere in range(indice_caractere+1, len(expressao)):
        if re.search(OPERACOES, expressao[caractere]) == None:
            if expressao[caractere] != ')':
                SEGUNDO_NUMERO += str(expressao[caractere])
            else:
                continue
        else:
            break
    #Condição em que se verifica se tem um número negativo mais á esquerda, se não tiver é null.
    if PRIMEIRO_NUMERO == '':
        return None, SEGUNDO_NUMERO, adiciona_sinal

    return PRIMEIRO_NUMERO, SEGUNDO_NUMERO, adiciona_sinal

#Função para verificar se ainda existe uma operação a ser resolvida na expressão.
def temOperacao(expressao_testada):
    #Regex que identifica numeros e operações (se existir uma operação obrigatoriamente deve existir numeros ao redor dela).
    OPERACOES = re.compile('([0-9]{1,}(\.)?([0-9]{0,})((([\^*\/+\-])))[0-9](\.)?([0-9]{0,})|(r[0-9](\.)?([0-9]{0,})))')
    busca_operacoes = re.search(OPERACOES, expressao_testada)
    return busca_operacoes

#Função para identificar a operação a ser realizada.
def identificaOperacao(inicio_parenteses, fim_parenteses, expressao):
    lista_operacoes = ['^', 'r', '*', '/', '+', '-']
    
    for operacao in lista_operacoes:
        for indice, caractere in enumerate(expressao[inicio_parenteses:fim_parenteses]):
            if caractere == operacao:
                PRIMEIRO_NUMERO, SEGUNDO_NUMERO, adiciona_sinal = identificaNumerais(expressao[inicio_parenteses:fim_parenteses], indice)
                #Se o primeiro numero é None, quer dizer que se trata de um número negativo (Por exemplo: -125, a operação é -, mas o primeiro numero é None.)
                if PRIMEIRO_NUMERO == None and operacao == '-':
                    continue
                #Se for exponenciação
                if operacao == '^':
                    resultado = exponenciacao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                    return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                #Se for raiz
                elif operacao == 'r':
                    resultado = raiz(SEGUNDO_NUMERO)
                    return '{}{}'.format(operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                #Se for multiplicação
                elif operacao == '*':
                    resultado = multiplicacao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                    return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                #Se for divisão
                elif operacao == '/':
                    resultado = divisao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                    return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                #Se for adição
                elif operacao == '+':
                    resultado = adicao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                    return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                #Se for subtração
                elif operacao == '-':
                    resultado = subtracao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                    return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal
    return None, None, None

#Função para remover os parênteses.
def removeParenteses(expressao):
    #Regex para identificar parênteses
    PARENTESES = re.compile('[\)\()]')
    expressao = re.sub(PARENTESES, '', expressao)
    return expressao