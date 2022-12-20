import time
import math
import xmpp
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

#Agente de raiz quadrada
class RaizAgente(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                print('Agente de Raiz Quadrada')
                print('Realizando a operação de raiz quadrada do número: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = math.sqrt(float(resultado[0]))
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                print('Resultado da operação de raiz quadrada: {msg.body}')

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())

#Agente de exponenciação
class ExponenciacaoAgente(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                print('Agente de Exponenciação')
                print('Realizando a operação de exponenciação entre os números: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) ** float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                print('Resultado da operação de exponenciação: {msg.body}')

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())

#Agente de multiplicação
class MultiplicacaoAgente(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                print('Agente de Multiplicação')
                print('Realizando a operação de multiplicação entre os números: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) * float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                print('Resultado da operação de multiplicação: {msg.body}')

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())

#Agente de divisão
class DivisaoAgente(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                print('Agente de Divisão')
                print('Realizando a operação de divisão entre os números: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) / float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                print('Resultado da operação de multiplicação: {msg.body}')
                
    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())

#Agente de adição.
class AdicaoAgente(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                print('Agente de Adição')
                print('Realizando a operação de adição entre os números: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) + float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                print('Resultado da operação de adição: {msg.body}')

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())

#Agente de subtração.
class SubtracaoAgente(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                print('Agente de Subtração')
                print('Realizando a operação de subtração entre os números: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) - float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                print('Resultado da operação de subtração: {msg.body}')

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())

#Agente mestre, que identifica operações, quebra operações e manda as mesmas para os agentes resolverem.
class MestreAgente(Agent):    
    class QuebraExpressao(OneShotBehaviour):
        def __init__(self):
            super().__init__()
            self.expression = None
        
        @staticmethod
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
        
        @staticmethod
        #Função para identificar a operação a ser realizada.
        def identificaOperacao(self, inicio_parenteses, fim_parenteses, expressao):
            lista_operacoes = ['^', 'r', '*', '/', '+', '-']
            
            for operacao in lista_operacoes:
                for indice, caractere in enumerate(expressao[inicio_parenteses:fim_parenteses]):
                    if caractere == operacao:
                        PRIMEIRO_NUMERO, SEGUNDO_NUMERO, adiciona_sinal = self.identificaNumerais(expressao[inicio_parenteses:fim_parenteses], indice)
                        #Se o primeiro numero é None, quer dizer que se trata de um número negativo (Por exemplo: -125, a operação é -, mas o primeiro numero é None.)
                        if PRIMEIRO_NUMERO == None and operacao == '-':
                            continue
                        #Se for exponenciação
                        if operacao == '^':
                            msg = Message(to='exponenciacao_agent@localhost/5222')
                            msg.body = str(PRIMEIRO_NUMERO) + " " + str(SEGUNDO_NUMERO)
                            self.send(msg)
                            print('MestreAgente: Enviando expressão para o Agente de Exponenciação: {msg.body}')
                            msg = self.receive(timeout=60)
                            if msg:
                                resultado = msg.body
                            return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                        #Se for raiz
                        elif operacao == 'r':
                            msg = Message(to='raiz_agent@localhost/5222')
                            msg.body = str(PRIMEIRO_NUMERO) + " " + str(SEGUNDO_NUMERO)
                            self.send(msg)
                            print('MestreAgente: Enviando expressão para o Agente de Raiz Quadrada: {msg.body}')
                            msg = self.receive(timeout=60)
                            if msg:
                                resultado = msg.body
                            return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                        #Se for multiplicação
                        elif operacao == '*':
                            msg = Message(to='multiplicacao_agent@localhost/5222')
                            msg.body = str(PRIMEIRO_NUMERO) + " " + str(SEGUNDO_NUMERO)
                            self.send(msg)
                            print('MestreAgente: Enviando expressão para o Agente de Multiplicação: {msg.body}')
                            msg = self.receive(timeout=60)
                            if msg:
                                resultado = msg.body
                            return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                        #Se for divisão
                        elif operacao == '/':
                            msg = Message(to='divisao_agent@localhost/5222')
                            msg.body = str(PRIMEIRO_NUMERO) + " " + str(SEGUNDO_NUMERO)
                            self.send(msg)
                            print('MestreAgente: Enviando expressão para o Agente de Divisão: {msg.body}')
                            msg = self.receive(timeout=60)
                            if msg:
                                resultado = msg.body
                            return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                        #Se for adição
                        elif operacao == '+':
                            msg = Message(to='adicao_agent@localhost/5222')
                            msg.body = str(PRIMEIRO_NUMERO) + " " + str(SEGUNDO_NUMERO)
                            self.send(msg)
                            print('MestreAgente: Enviando expressão para o Agente de Adição: {msg.body}')
                            msg = self.receive(timeout=60)
                            if msg:
                                resultado = msg.body
                            return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

                        #Se for subtração
                        elif operacao == '-':
                            msg = Message(to='subtracao_agent@localhost/5222')
                            msg.body = str(PRIMEIRO_NUMERO) + " " + str(SEGUNDO_NUMERO)
                            self.send(msg)
                            print('MestreAgente: Enviando expressão para o Agente de Subtração: {msg.body}')
                            msg = self.receive(timeout=60)
                            if msg:
                                resultado = msg.body
                            return '{}{}{}'.format(PRIMEIRO_NUMERO, operacao, SEGUNDO_NUMERO), resultado, adiciona_sinal

            return None, None, None

        async def inicio(self):
            expressao = input('Digite a expressão a ser calculada: ')
            if expressao == ' ':
                await self.agent.stop()
            expressao = expressao.replace(' ', '')
            expressao = expressao.replace("–", "-")
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
            print('Resultado final da expressão: {}'.format(expressao))

    async def setup(self):
        self.add_behaviour(self.SolveExpression())

if __name__ == "__main__":
    debug = False
    client = xmpp.Client('localhost',debug=[])
    client.connect(server=('localhost',5222), use_srv=False)

    exponenciacao = ExponenciacaoAgente("exponenciacao_agent@localhost/5222", "123")
    operacao = exponenciacao.start()
    operacao.result()

    raiz = RaizAgente("raiz_agent@localhost/5222", "123")
    operacao = raiz.start()
    operacao.result()

    multiplicacao = MultiplicacaoAgente("multiplicacao_agent@localhost/5222", "123")
    operacao = multiplicacao.start()
    operacao.result()

    divisao = DivisaoAgente("divisao_agent@localhost/5222", "123")
    operacao = divisao.start()
    operacao.result()

    soma = AdicaoAgente("adicao_agent@localhost/5222", "123")
    operacao = soma.start()
    operacao.result()

    subtracao = SubtracaoAgente("subtracao_agent@localhost/5222", "123")
    operacao = subtracao.start()
    operacao.result()

    mestre = MestreAgente("mestre_agent@localhost/5222", "123")
    operacao = mestre.start()
    operacao.result()

    while mestre.is_alive():
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            soma.stop()
            subtracao.stop()
            multiplicacao.stop()
            divisao.stop()
            exponenciacao.stop()
            raiz.stop()
            mestre.stop()
            break
