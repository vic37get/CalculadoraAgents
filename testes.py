from unittest import main, TestCase
from master import Master

expressao = '25+5'
expressao2 = "23 + 12 - 55 + 2 + 4 - 8 / (2+5) - (1+2)"
expressao2n = "23 + 12 - 55 + 2 + 4 - 8 / (2+5) - (1+2)"

class Test(TestCase):
    def testExpressao(self):
        self.assertEquals(Master(expressao.replace(' ', '')), str(eval(expressao)))

    def testExpressao2(self):
        self.assertEquals(Master(expressao2.replace(' ', '')), str(eval(expressao2n)))


if __name__ == '__main__':
    main()
