import math
import time

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

debug = True

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



#_______________________________________________
