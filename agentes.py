import pade

#Operações da calculadora

class AdicaoAgent(pade.Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
    
    def on_start(self):
        pass

    def adicao(num1, num2):
        print('Realizando a operação de soma entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)+int(num2)
        except ValueError:
            resultado = float(num1)+float(num2)
        print('Resultado da operação: {}'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '+':
            num1, num2 = msg.content
            result = self.adicao(num1, num2)
            msg.respond(result)

class SubtracaoAgent(pade.Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
    
    def on_start(self):
        pass

    def subtracao(num1, num2):
        print('Realizando a operação de subtração entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)-int(num2)
        except ValueError:
            resultado = float(num1)-float(num2)
        print('Resultado da operação: {}'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '-':
            num1, num2 = msg.content
            result = self.subtracao(num1, num2)
            msg.respond(result)

class DivisaoAgent(pade.Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
    
    def on_start(self):
        pass

    def divisao(num1, num2):
        print('Realizando a operação de divisão entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)/int(num2)
        except ValueError:
            resultado = float(num1)/float(num2)
        print('Resultado da operação: {}'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '/':
            num1, num2 = msg.content
            result = self.divisao(num1, num2)
            msg.respond(result)

class MultiplicacaoAgent(pade.Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
    
    def on_start(self):
        pass

    def multiplicacao(num1, num2):
        print('Realizando a operação de multiplicação entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)*int(num2)
        except ValueError:
            resultado = float(num1)*float(num2)
        print('Resultado da operação: {}'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '*':
            num1, num2 = msg.content
            result = self.multiplicacao(num1, num2)
            msg.respond(result)

class ExponenciacaoAgent(pade.Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
    
    def on_start(self):
        pass

    def exponenciacao(num1, num2):
        print('Realizando a operação de exponenciação entre os números {} e {}'.format(num1, num2))
        try:
            resultado = int(num1)**int(num2)
        except ValueError:
            resultado = float(num1)**float(num2)
        print('Resultado da operação: {}'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == '^':
            num1, num2 = msg.content
            result = self.exponenciacao(num1, num2)
            msg.respond(result)

class RaizAgent(pade.Agent):
    def __init__(self, aid):
        super().__init__(aid=aid, debug=False)
    
    def on_start(self):
        pass

    def raiz(num1):
        print('Realizando a operação de raiz quadrada do número {}'.format(num1))
        try:
            resultado = int(num1)**1/2
        except ValueError:
            resultado = float(num1)**1/2
        print('Resultado da operação: {}'.format(resultado))
        return resultado
    
    def on_message(self, msg):
        if msg.body == 'r':
            num1 = msg.content
            result = self.raiz(num1)
            msg.respond(result)