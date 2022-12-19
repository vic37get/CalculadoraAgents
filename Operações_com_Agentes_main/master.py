import time
import math
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

debug = True


def achaOperacao(equacao):
    operacoes = ["=", "+", "-", "/", "*", "#", "^", "("]
    maior_operacao = ["=", ""]
    for i in range(len(equacao)):
        if equacao[i] in operacoes:
            if operacoes.index(maior_operacao[0]) < operacoes.index(equacao[i]):
                maior_operacao[0] = equacao[i]
    maior_operacao[1] = equacao.index(maior_operacao[0])  # Guarda a posição do maiorOperador encontrado
    return maior_operacao


def achaOperandos(equacao, maior_operacao):
    operacoes = ["=", "-", "+", "/", "*", "#", "^"]
    operandos = ["", "", 0, 0]
    for i in range(len(equacao)):
        if equacao[i] == maior_operacao:
            for a in range(i - 1, -1, -1):
                if equacao[a] in operacoes:
                    break
                operandos[0] = str(equacao[a]) + operandos[0]
                operandos[2] += 1

            for b in range(i + 1, len(equacao)):
                if equacao[b] in operacoes:
                    return operandos
                operandos[1] = operandos[1] + str(equacao[b])
                operandos[3] += 1
                if b + 1 == len(equacao):
                    return operandos


class SumAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                if debug:
                    print(f'SumAgent: Mensagem recebida, fazendo soma com os numeros: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) + float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                if debug:
                    print(f'SumAgent: Resposta enviada, resultado da soma: {msg.body}')
                    time.sleep(5)

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class SubtractionAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                if debug:
                    print(f'SubtractionAgent: Mensagem recebida, fazendo subtracao com os numeros: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) - float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                if debug:
                    print(f'SubtractionAgent: Resposta enviada, resultado da subtracao: {msg.body}')
                    time.sleep(5)

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class MultiplicationAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                if debug:
                    print(f'MultiplicationAgent: Mensagem recebida, fazendo multiplicacao com os numeros: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) * float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                if debug:
                    print(f'MultiplicationAgent: Resposta enviada, resultado da multiplicacao: {msg.body}')
                    time.sleep(5)

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class DivisionAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                if debug:
                    print(f'DivisionAgent: Mensagem recebida, fazendo divisao com os numeros: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) / float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                if debug:
                    print(f'DivisionAgent: Resposta enviada, resultado da divisao: {msg.body}')
                    time.sleep(5)

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class PowerAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                if debug:
                    print(f'PowerAgent: Mensagem recebida, fazendo potencia com os numeros: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = float(resultado[0]) ** float(resultado[1])
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                if debug:
                    print(f'PowerAgent: Resposta enviada, resultado da potencia: {msg.body}')
                    time.sleep(5)

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class SquareRootAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):
            msg = await self.receive()
            if msg:
                if debug:
                    print(f'SquareRootAgent: Mensagem recebida, fazendo raiz quadrada do numero: {msg.body}')
                resultado = msg.body.split(" ")
                resultado = math.sqrt(float(resultado[0]))
                sender = msg.sender
                msg = Message(to=str(sender))
                msg.body = str(resultado)
                await self.send(msg)
                if debug:
                    print(f'SquareRootAgent: Resposta enviada, resultado da raiz quadrada: {msg.body}')
                    time.sleep(5)

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class ParenthesisAgent(Agent):
    class ReceiveMsg(CyclicBehaviour):
        async def run(self):

            self.expression = await self.receive(timeout=60)
            if debug:
                print(f'ParenthesisAgent: Mensagem recebida: {self.expression.body}')
            self.expression = self.expression.body.split(" ")

            while len(self.expression) > 1:

                f = achaOperacao(self.expression)
                maior_operacao = f[0]
                x = int(f[1])

                operandos = achaOperandos(self.expression, maior_operacao)
                if maior_operacao != "#":
                    num1 = float(operandos[0])
                    num2 = float(operandos[1])
                else:
                    num2 = float(operandos[1])

                if maior_operacao == "^":
                    msg = Message(to='power_agent@localhost/5222')
                    msg.body = str(num1) + " " + str(num2)
                    await self.send(msg)
                    if debug:
                        print(f'ParenthesisAgent: Enviando operandos para operacao de potencia: {msg.body}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression[x - operandos[2]] = msg.body
                elif maior_operacao == "#":
                    msg = Message(to='squareroot_agent@localhost/5222')
                    msg.body = str(num2)
                    await self.send(msg)
                    if debug:
                        print(f'ParenthesisAgent: Enviando operandos para operacao de raiz quadrada: {msg.body}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression[x - operandos[2]] = msg.body
                elif maior_operacao == "*":
                    msg = Message(to='multiplication_agent@localhost/5222')
                    msg.body = str(num1) + " " + str(num2)
                    await self.send(msg)
                    if debug:
                        print(f'ParenthesisAgent: Enviando operandos para operacao de multiplicacao: {msg.body}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression[x - operandos[2]] = msg.body
                elif maior_operacao == "/":
                    msg = Message(to='division_agent@localhost/5222')
                    msg.body = str(num1) + " " + str(num2)
                    await self.send(msg)
                    if debug:
                        print(f'ParenthesisAgent: Enviando operandos para operacao de divisao: {msg.body}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression[x - operandos[2]] = msg.body
                elif maior_operacao == "+":
                    msg = Message(to='sum_agent@localhost/5222')
                    msg.body = str(num1) + " " + str(num2)
                    await self.send(msg)
                    if debug:
                        print(f'ParenthesisAgent: Enviando operandos para operacao de soma: {msg.body}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression[x - operandos[2]] = msg.body
                elif maior_operacao == "-" or maior_operacao == "–":
                    msg = Message(to='subtract_agent@localhost/5222')
                    msg.body = str(num1) + " " + str(num2)
                    await self.send(msg)
                    if debug:
                        print(f'ParenthesisAgent: Enviando operandos para operacao de subtracao: {msg.body}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression[x - operandos[2]] = msg.body

                for g in range(x - operandos[2] + 1, x + operandos[3] + 1):
                    self.expression.pop(x - operandos[2] + 1)

                if len(self.expression) == 1:
                    msg = Message(to='coordinator_agent@localhost/5222')
                    msg.body = self.expression[0]
                    await self.send(msg)
                    break

    async def setup(self):
        self.add_behaviour(self.ReceiveMsg())


class CoordinatorAgent(Agent):    
    class SolveExpression(OneShotBehaviour):
        def __init__(self):
            super().__init__()
            self.expression = None
        
        @staticmethod
        def match_parenthesis(expression):
            for i in range(len(expression)):
                if expression[i] == ")":
                    return i

        async def run(self):
            self.expression = input('Digite a expressão: ')
            if self.expression == ' ':
                await self.agent.stop()
            self.expression = self.expression.split(" ")

            while len(self.expression) != 1:

                f = achaOperacao(self.expression)
                maior_operacao = f[0]
                x = int(f[1])

                expressao = ""
                for i in self.expression:
                    expressao += " " + i
                print(f'CoordinatorAgent: Expressao a ser resolvida: {expressao}')

                if maior_operacao == "(":
                    interior_parenthesis = ""
                    final_index = self.match_parenthesis(self.expression)
                    initial_index = 0
                    self.expression.pop(final_index)
                    for a in range(final_index - 1, -1, -1):
                        if self.expression[a] == '(':
                            initial_index = a
                            break
                    for a in range(initial_index + 1, final_index):
                        interior_parenthesis += " " + self.expression[a]
                    for a in range(final_index - 1, initial_index - 1, -1):
                        self.expression.pop(a)
                    msg = Message(to='parenthesis_agent@localhost/5222')
                    msg.body = interior_parenthesis
                    await self.send(msg)
                    if debug:
                        print(
                            f'CoordinatorAgent: Enviando operacao do parenteses para o agente de parenteses:'
                            f'{interior_parenthesis}')
                    msg = await self.receive(timeout=60)
                    if msg:
                        self.expression.insert(initial_index, msg.body)
                        if debug:
                            print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')
                else:
                    operandos = achaOperandos(self.expression, maior_operacao)
                    if maior_operacao != "#":
                        num1 = float(operandos[0])
                        num2 = float(operandos[1])
                    else:
                        num2 = float(operandos[1])

                    if maior_operacao == "^":
                        msg = Message(to='power_agent@localhost/5222')
                        msg.body = str(num1) + " " + str(num2)
                        await self.send(msg)
                        if debug:
                            print(f'CoordinatorAgent: Enviando operandos para operacao de potencia: {msg.body}')
                        msg = await self.receive(timeout=60)
                        if msg:
                            self.expression[x - operandos[2]] = msg.body
                            if debug:
                                print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')
                    elif maior_operacao == "#":
                        msg = Message(to='squareroot_agent@localhost/5222')
                        msg.body = str(num2)
                        await self.send(msg)
                        if debug:
                            print(f'CoordinatorAgent: Enviando operandos para operacao de raiz quadrada: {msg.body}')
                        msg = await self.receive(timeout=60)
                        if msg:
                            self.expression[x - operandos[2]] = msg.body
                            if debug:
                                print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')
                    elif maior_operacao == "*":
                        msg = Message(to='multiplication_agent@localhost/5222')
                        msg.body = str(num1) + " " + str(num2)
                        await self.send(msg)
                        if debug:
                            print(f'CoordinatorAgent: Enviando operandos para operacao de multiplicacao: {msg.body}')
                        msg = await self.receive(timeout=60)
                        if msg:
                            self.expression[x - operandos[2]] = msg.body
                            if debug:
                                print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')
                    elif maior_operacao == "/":
                        msg = Message(to='division_agent@localhost/5222')
                        msg.body = str(num1) + " " + str(num2)
                        await self.send(msg)
                        if debug:
                            print(f'CoordinatorAgent: Enviando operandos para operacao de divisao: {msg.body}')
                        msg = await self.receive(timeout=60)
                        if msg:
                            self.expression[x - operandos[2]] = msg.body
                            if debug:
                                print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')
                    elif maior_operacao == "+":
                        msg = Message(to='sum_agent@localhost/5222')
                        msg.body = str(num1) + " " + str(num2)
                        await self.send(msg)
                        if debug:
                            print(f'CoordinatorAgent: Enviando operandos para operacao de soma: {msg.body}')
                        msg = await self.receive(timeout=60)
                        if msg:
                            self.expression[x - operandos[2]] = msg.body
                            if debug:
                                print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')
                    elif maior_operacao == "-" or maior_operacao == "–":
                        msg = Message(to='subtract_agent@localhost/5222')
                        msg.body = str(num1) + " " + str(num2)
                        await self.send(msg)
                        if debug:
                            print(f'CoordinatorAgent: Enviando operandos para operacao de subtracao: {msg.body}')
                        msg = await self.receive(timeout=60)
                        if msg:
                            self.expression[x - operandos[2]] = msg.body
                            if debug:
                                print(f'CoordinatorAgent: Resposta recebida, resultado da operacao: {msg.body}')

                    for g in range(x - operandos[2] + 1, x + operandos[3] + 1):
                        self.expression.pop(x - operandos[2] + 1)

                if len(self.expression) == 1:
                    print(f'Resultado da expressão encontrado: {self.expression[0]}')
                    await self.agent.stop()
                    break

    async def setup(self):
        self.add_behaviour(self.SolveExpression())


if __name__ == "__main__":
    debug = False

    soma = SumAgent("sum_agent@localhost/5222", "123")
    future = soma.start()
    future.result()
    # print('Soma inicializado')
    subtracao = SubtractionAgent("subtract_agent@localhost/5222", "123")
    future = subtracao.start()
    future.result()
    # print('Subtracao inicializado')
    multiplicacao = MultiplicationAgent("multiplication_agent@localhost/5222", "123")
    future = multiplicacao.start()
    future.result()
    # print('Multiplicacao inicializado')
    divisao = DivisionAgent("division_agent@localhost/5222", "123")
    future = divisao.start()
    future.result()
    # print('Divisao inicializado')
    potencia = PowerAgent("power_agent@localhost/5222", "123")
    future = potencia.start()
    future.result()
    # print('Potencia inicializado')
    raiz = SquareRootAgent("squareroot_agent@localhost/5222", "123")
    future = raiz.start()
    future.result()
    # print('Raiz inicializado')
    parenteses = ParenthesisAgent("parenthesis_agent@localhost/5222", "123")
    future = parenteses.start()
    future.result()
    # print('Parenteses inicializado')
    coordenador = CoordinatorAgent("coordinator_agent@localhost/5222", "123")
    future = coordenador.start()
    future.result()
    # print('Coordenador inicializado')

    while coordenador.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            soma.stop()
            subtracao.stop()
            multiplicacao.stop()
            divisao.stop()
            potencia.stop()
            raiz.stop()
            parenteses.stop()
            coordenador.stop()
            break
    print("Agents finished")
