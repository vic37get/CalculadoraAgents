import math
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


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


class RaizAgent(Agent):
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