import re
from pade.acl.aid import AID
from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop
from sys import argv

from agentes import *

class MasterAgent(Agent):
    def __init__(self, aid):
        super(MasterAgent, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Oi eu sou o agente principal\n')
    
    def on_start(self):
        pass

    #Função para buscar os parênteses em uma sentença.
    def buscaParenteses(self, expressao):
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
    def identificaNumerais(self, expressao, indice_caractere):
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
    def temOperacao(self, expressao_testada):
        #Regex que identifica numeros e operações (se existir uma operação obrigatoriamente deve existir numeros ao redor dela).
        OPERACOES = re.compile('([0-9]{1,}(\.)?([0-9]{0,})((([\^*\/+\-])))[0-9](\.)?([0-9]{0,})|(r[0-9](\.)?([0-9]{0,})))')
        busca_operacoes = re.search(OPERACOES, expressao_testada)
        return busca_operacoes

    #Função para identificar a operação a ser realizada.
    def identificaOperacao(self, inicio_parenteses, fim_parenteses, expressao):
        lista_operacoes = ['^', 'r', '*', '/', '+', '-']
        
        for operacao in lista_operacoes:
            for indice, caractere in enumerate(expressao[inicio_parenteses:fim_parenteses]):
                if caractere == operacao:
                    PRIMEIRO_NUMERO, SEGUNDO_NUMERO, adiciona_sinal = self.identificaNumerais(expressao[inicio_parenteses:fim_parenteses], indice)
                    display_message(self.aid.localname, "{} {} {}\n".format(PRIMEIRO_NUMERO, SEGUNDO_NUMERO, adiciona_sinal))
                    #Se o primeiro numero é None, quer dizer que se trata de um número negativo (Por exemplo: -125, a operação é -, mas o primeiro numero é None.)
                    if PRIMEIRO_NUMERO == None and operacao == '-':
                        continue
                    #Se for exponenciação
                    if operacao == '^':
                        agent_name = 'agente_exponenciacao_{}@localhost:{}'.format(100, 100)
                        agent_expo = ExponenciacaoAgent(AID(name=agent_name))
                        resultado = agent_expo.exponenciacao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                        return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                    #Se for raiz
                    elif operacao == 'r':
                        agent_name = 'agente_raiz_{}@localhost:{}'.format(1020, 1020)
                        agent_raiz = RaizAgent(AID(name=agent_name))
                        resultado = agent_raiz.raiz(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                        return '{}{}'.format(operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                    #Se for multiplicação
                    elif operacao == '*':
                        agent_name = 'agente_multiplicacao_{}@localhost:{}'.format(1040, 1040)
                        agent_mult = MultiplicacaoAgent(AID(name=agent_name))
                        resultado = agent_mult.multiplicacao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                        return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                    #Se for divisão
                    elif operacao == '/':
                        agent_name = 'agente_divisao_{}@localhost:{}'.format(1060, 1060)
                        agent_div = DivisaoAgent(AID(name=agent_name))
                        resultado = agent_div.divisao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                        return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                    #Se for adição
                    elif operacao == '+':
                        agent_name = 'agente_adicao_{}@localhost:{}'.format(1080, 1080)
                        agent_adc = AdicaoAgent(AID(name=agent_name))
                        resultado = agent_adc.adicao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                        return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                    #Se for subtração
                    elif operacao == '-':
                        agent_name = 'agente_subtracao_{}@localhost:{}'.format(2000, 2000)
                        agent_sub = SubtracaoAgent(AID(name=agent_name))
                        resultado = agent_sub.subtracao(PRIMEIRO_NUMERO, SEGUNDO_NUMERO)
                        return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal
        return None, None, None

    #Função para remover os parênteses.
    def removeParenteses(self, expressao):
        #Regex para identificar parênteses
        PARENTESES = re.compile('[\)\()]')
        expressao = re.sub(PARENTESES, '', expressao)
        return expressao
                
                
    #Função que é o mestre, começa buscando as expressões entre parênteses. (precedencia)
    def Master(self, expressao):
        #Se existe parenteses na expressão.
        parenteses = True
        #Se a expressao ja está resolvida.
        resolvida = False
        
        while parenteses == True:
            #Encontra os parenteses
            inicio_parenteses, fim_parenteses = self.buscaParenteses(expressao)
            if inicio_parenteses != None or fim_parenteses != None:
                parenteses = True
                #Verifica se tem operação dentro do parentese encontrado
                if self.temOperacao(expressao[inicio_parenteses:fim_parenteses]) != None:
                    #Se houver, identifica a operação, chama a função que calcula aquela expressao e retorna o resultado.
                    EXPRESSAO_RESOLVIDA, RESULTADO, ADICIONA_SINAL = self.identificaOperacao(inicio_parenteses, fim_parenteses, expressao)
                    #Após calcular, substitui na expressao original, a expressão resolvida pelo resultado dela.
                    if ADICIONA_SINAL == True and RESULTADO>=0:
                        expressao = expressao.replace(str(EXPRESSAO_RESOLVIDA), '+{}'.format(RESULTADO))
                    else:
                        expressao = expressao.replace(str(EXPRESSAO_RESOLVIDA), str(RESULTADO))
                #Caso não exista operações a serem resolvidas dentro do parentese
                else:
                    #Remove os parenteses da expressao.
                    exp_sem_parenteses = self.removeParenteses(expressao[inicio_parenteses:fim_parenteses])
                    #Remove da expressao original os parenteses.
                    expressao = expressao.replace(expressao[inicio_parenteses:fim_parenteses], exp_sem_parenteses)
            else:
                #A expressao original nao tem mais parenteses.
                parenteses = False
        
        
        #Enquanto a expressao não estiver resolvida.
        while(resolvida == False):
            #Verifica se existe operação
            if self.temOperacao(expressao) != None:
                #Se houver, identifica a operação, chama a função que calcula aquela expressao e retorna o resultado.
                EXPRESSAO_RESOLVIDA, RESULTADO, ADICIONA_SINAL = self.identificaOperacao(inicio_parenteses, fim_parenteses, expressao)
                #Após calcular, substitui na expressao original, a expressão resolvida pelo resultado dela.
                if ADICIONA_SINAL == True and RESULTADO>=0:
                        expressao = expressao.replace(str(EXPRESSAO_RESOLVIDA), '+{}'.format(RESULTADO))
                else:
                    expressao = expressao.replace(str(EXPRESSAO_RESOLVIDA), str(RESULTADO))
            else:
                #A expressão está resolvida.
                resolvida = True
        display_message(self.aid.localname,'EXPRESSAO RETORNADA: {}'.format(expressao))
        return expressao
    
    # def on_message(self, msg):
    #     if msg.body == '+':
    #         num1, num2 = msg.content
    #         result = self.adicao(num1, num2)
    #         msg.respond(result)


if __name__ == '__main__':
    expressao = argv[1]
    expressao = expressao.replace(" ", "")
    expressao = expressao.replace("–", "-")
    agent_name = 'agente_resultado_expressao_{}@localhost:{}'.format(1, 1)
    agente_hello = MasterAgent(AID(name=agent_name))
    agente_hello.Master(expressao)