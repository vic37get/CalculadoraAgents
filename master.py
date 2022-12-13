import re

from operacoes import *

#Função para buscar os parênteses em uma sentença.
def find_parens(s):
    toret = []
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret.append((pstack.pop(),i+1))

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret

#Função para identificar os números envolvidos na operação, pegando a partir do indice do simbolo da operação
def identificaNumerais(expressao, indice_caractere):
    OPERACOES = re.compile('(((raiz)|([\^*\/+\-])))')
    NUMERO = re.compile('(\-?[0-9]{1,}(\.)?([0-9]{0,}))')
    #TENTAR CONSTRUIR UMA ESTRATÉGIA QUE PERMITE PEGAR O SINAL NEGATIVO SE APÓS DELE NÃO VIER UM NÚMERO. CONVERTENDO ESSE NÚMERO PARA -NUMERO EXEMPLO 55, -55.
    INICIO = ''
    FIM = ''
    for caractere in range(indice_caractere-1, -1, -1):
        if re.search(OPERACOES, expressao[caractere]) == None:
            if expressao[caractere] != '(':
                INICIO = str(expressao[caractere]) + INICIO
            else:
                continue
        else:
            break

    for caractere in range(indice_caractere+1, len(expressao)):
        if re.search(OPERACOES, expressao[caractere]) == None:
            if expressao[caractere] != ')':
                FIM += str(expressao[caractere])
            else:
                continue
        else:
            break
    #Condição em que se tem um número negativo mais á esquerda
    if INICIO == '':
        return None, FIM
    return INICIO, FIM

def temOperacao(expressao_testada):
    OPERACOES = re.compile('([0-9]{1,}(\.)?([0-9]{0,})(((raiz)|([\^*\/+\-])))[0-9](\.)?([0-9]{0,}))')
    busca_operacoes = re.search(OPERACOES, expressao_testada)
    return busca_operacoes


#Função para identificar a operação a ser realizada.
def identificaOperacao(inicio_parenteses, fim_parenteses, expressao):
    lista_operacoes = ['^', 'raiz', '*', '/', '+', '-']
    for operacao in lista_operacoes:
        for indice, caractere in enumerate(expressao[inicio_parenteses:fim_parenteses]):
            if caractere == operacao:
                INICIO, FIM = identificaNumerais(expressao[inicio_parenteses:fim_parenteses], indice)
                if INICIO == None:
                    return '{}{}'.format(FIM, operacao), FIM
                if operacao == '^':
                    resultado = exponenciacao(INICIO, FIM)
                    return '{}{}{}'.format(INICIO, operacao, FIM), resultado

                elif operacao == 'raiz':
                    resultado = raiz(INICIO, FIM)
                    return '{}{}{}'.format(INICIO, operacao, FIM), resultado

                elif operacao == '*':
                    resultado = multiplicacao(INICIO, FIM)
                    return '{}{}{}'.format(INICIO, operacao, FIM), resultado
                    
                elif operacao == '/':
                    resultado = divisao(INICIO, FIM)
                    return '{}{}{}'.format(INICIO, operacao, FIM), resultado

                elif operacao == '+':
                    resultado = adicao(INICIO, FIM)
                    return '{}{}{}'.format(INICIO, operacao, FIM), resultado
                    
                elif operacao == '-':
                    resultado = subtracao(INICIO, FIM)
                    return '{}{}{}'.format(INICIO, operacao, FIM), resultado
    return None, None

#Função para remover os parênteses.
def removeParenteses(expressao):
    PARENTESES = re.compile('[\)\()]')
    expressao = re.sub(PARENTESES, '', expressao)
    return expressao
            
#Função que é o mestre, começa buscando as expressões entre parênteses. (precedencia)
def Master(expressao):
    parenteses = find_parens(expressao)
    while parenteses:
        #print('\n')
        print(expressao)
        inicio_parenteses, fim_parenteses = parenteses.pop(0)
        if temOperacao(expressao[inicio_parenteses:fim_parenteses]) != None:
            EXPRESSAO_RESOLVIDA, RESULTADO = identificaOperacao(inicio_parenteses, fim_parenteses, expressao)
            expressao = expressao.replace(str(EXPRESSAO_RESOLVIDA), str(RESULTADO))
        else:
            exp_sem_parenteses = removeParenteses(expressao[inicio_parenteses:fim_parenteses])
            expressao = expressao.replace(expressao[inicio_parenteses:fim_parenteses], exp_sem_parenteses)
            
    print('fim')

# entrada = "23 + 12 - 55 + 2 + 4 - 8 / (2+5) - (1+2)"
#Falta lidar com esse exemplo: O que fazer quando temos um simbolo de operação seguido de um número negativo: exemplo 2/-3
#entrada = "23 + 12 - 55 + 2 + 4 - 8 / ((2*3)+5-(4/2)-12^2+(5/5))"
if __name__ == "__main__":
    # entrada = '(-136+15)'
    entrada = "23 + 12 - 55 + 2 + 4 - 8 / (2+5) - (1+2)"
    entrada = entrada.replace(' ', '')
    Master(entrada)