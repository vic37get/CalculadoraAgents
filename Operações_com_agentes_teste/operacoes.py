from pade.core.agent import Agent
from pade.misc.utility import display_message


#Operações da calculadora
class AdicaoAgent(Agent):
    def __init__(self, aid):
        super(AdicaoAgent, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Agente de Adição')
    
    def on_start(self):
        pass

    def adicao(self, num1, num2):
        display_message(self.aid.localname,'Realizando a operação de adição entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)+int(num2)
        except ValueError:
            resultado = float(num1)+float(num2)
        display_message(self.aid.localname,'Resultado da operação de adição: {}\n'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '+':
            num1, num2 = msg.content
            result = self.adicao(num1, num2)
            msg.respond(result)

class SubtracaoAgent(Agent):
    def __init__(self, aid):
        super(SubtracaoAgent,self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Agente de Subtração')
    
    def on_start(self):
        pass

    def subtracao(self, num1, num2):
        display_message(self.aid.localname,'Realizando a operação de subtração entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)-int(num2)
        except ValueError:
            resultado = float(num1)-float(num2)
        display_message(self.aid.localname,'Resultado da operação de subtração: {}\n'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '-':
            num1, num2 = msg.content
            result = self.subtracao(num1, num2)
            msg.respond(result)

class DivisaoAgent(Agent):
    def __init__(self, aid):
        super(DivisaoAgent,self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Agente de Divisão')
    
    def on_start(self):
        pass

    def divisao(self, num1, num2):
        display_message(self.aid.localname,'Realizando a operação de divisão entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)/int(num2)
        except ValueError:
            resultado = float(num1)/float(num2)
        display_message(self.aid.localname,'Resultado da operação de divisão: {}\n'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '/':
            num1, num2 = msg.content
            result = self.divisao(num1, num2)
            msg.respond(result)

class MultiplicacaoAgent(Agent):
    def __init__(self, aid):
        super(MultiplicacaoAgent, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Agente de Multiplicação')
    
    def on_start(self):
        pass

    def multiplicacao(self, num1, num2):
        display_message(self.aid.localname,'Realizando a operação de multiplicação entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)*int(num2)
        except ValueError:
            resultado = float(num1)*float(num2)
        display_message(self.aid.localname,'Resultado da operação de multiplicação: {}\n'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '*':
            num1, num2 = msg.content
            result = self.multiplicacao(num1, num2)
            msg.respond(result)

class ExponenciacaoAgent(Agent):
    def __init__(self, aid):
        super(ExponenciacaoAgent, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Agente de Exponenciação')
    
    def on_start(self):
        pass

    def exponenciacao(self, num1, num2):
        display_message(self.aid.localname,'Realizando a operação de exponenciação entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)**int(num2)
        except ValueError:
            resultado = float(num1)**float(num2)
        display_message(self.aid.localname,'Resultado da operação de exponenciação: {}\n'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '^':
            num1, num2 = msg.content
            result = self.exponenciacao(num1, num2)
            msg.respond(result)

class RaizAgent(Agent):
    def __init__(self, aid):
        super(RaizAgent, self).__init__(aid=aid, debug=False)
        display_message(self.aid.localname, 'Agente de Raiz quadrada')
    
    def on_start(self):
        pass

    def raiz(self, num1):
        display_message(self.aid.localname,'Realizando a operação de raiz quadrada do número {}'.format(num1))
        try:
            resultado = int(num1)**1/2
        except ValueError:
            resultado = float(num1)**1/2
        display_message(self.aid.localname,'Resultado da operação de raiz quadrada: {}\n'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == 'r':
            num1 = msg.content
            result = self.raiz(num1)
            msg.respond(result)