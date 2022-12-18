import re
from sys import argv

from agentes import *
from pade.acl.aid import AID
from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop


class MasterAgent(Agent):
    def __init__(self, aid):
        super(MasterAgent, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Oi eu sou o agente principal\n')
    
    def on_start(self):
        pass
  
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
        display_message(self.aid.localname, 'Resultado da expressão: {}'.format(expressao))
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