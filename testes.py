from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv


class Remetente(Agent):
    def __init__(self, aid):
        super(Remetente, self).__init__(aid=aid, debug=False)

    def on_start(self):
        display_message(self.aid.localname, 'Enviando Mensagem')
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('destinatario'))
        message.set_content('Ola')
        self.send(message)

    def react(self, message):
        pass


class Destinatario(Agent):
    def __init__(self, aid):
        super(Destinatario, self).__init__(aid=aid, debug=False)

    def react(self, message):
        display_message(self.aid.localname, 'Mensagem recebida')


if __name__ == '__main__':

    agents = list()
    remetente_agent = Remetente(AID(name='remetente'))
    agents.append(remetente_agent)
    
    destinatario_agent = Destinatario(AID(name='destinatario'))
    agents.append(destinatario_agent)


    start_loop(agents)