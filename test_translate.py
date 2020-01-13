import unittest
import translator

class TestTranslate(unittest.TestCase):

    def test_translateReturnZero(self):
        self.assertEqual(translator.translate(0), "zero")
        self.assertEqual(translator.translate(00000), "zero")
        self.assertEqual(translator.translate(-0), "zero")
        self.assertEqual(translator.translate(+0), "zero")

    def test_translateReturnTensThousandsNumbers(self):
        self.assertEqual(translator.translate(10000), "dez mil")
        self.assertEqual(translator.translate(11000), "onze mil")
        self.assertEqual(translator.translate(15000), "quinze mil")
        self.assertEqual(translator.translate(19000), "dezenove mil")
        self.assertEqual(translator.translate(20000), "vinte mil")
        self.assertEqual(translator.translate(21000), "vinte e um mil")
        self.assertEqual(translator.translate(25000), "vinte e cinco mil")
        self.assertEqual(translator.translate(50000), "cinquenta mil")
        self.assertEqual(translator.translate(90000), "noventa mil")
        self.assertEqual(translator.translate(99000), "noventa e nove mil")

    def test_translateReturnThousandNumbers(self):
        self.assertEqual(translator.translate(1000), "um mil")
        self.assertEqual(translator.translate(2000), "dois mil")
        self.assertEqual(translator.translate(3000), "três mil")
        self.assertEqual(translator.translate(4000), "quatro mil")
        self.assertEqual(translator.translate(5000), "cinco mil")
        self.assertEqual(translator.translate(9000), "nove mil")

    def test_translateReturnHundredNumbers(self):
        self.assertEqual(translator.translate(100), "cem")
        self.assertEqual(translator.translate(101), "cento e um")
        self.assertEqual(translator.translate(105), "cento e cinco")
        self.assertEqual(translator.translate(110), "cento e dez")
        self.assertEqual(translator.translate(111), "cento e onze")
        self.assertEqual(translator.translate(112), "cento e doze")
        self.assertEqual(translator.translate(115), "cento e quinze")
        self.assertEqual(translator.translate(119), "cento e dezenove")
        self.assertEqual(translator.translate(120), "cento e vinte")
        self.assertEqual(translator.translate(200), "duzentos")
        self.assertEqual(translator.translate(201), "duzentos e um")
        self.assertEqual(translator.translate(205), "duzentos e cinco")
        self.assertEqual(translator.translate(209), "duzentos e nove")
        self.assertEqual(translator.translate(210), "duzentos e dez")
        self.assertEqual(translator.translate(299), "duzentos e noventa e nove")
        self.assertEqual(translator.translate(300), "trezentos")
        self.assertEqual(translator.translate(500), "quinhentos")
        self.assertEqual(translator.translate(900), "novecentos")
        self.assertEqual(translator.translate(999), "novecentos e noventa e nove")

    def test_translateReturnTensNumbers(self):
        self.assertEqual(translator.translate(10), "dez")
        self.assertEqual(translator.translate(11), "onze")
        self.assertEqual(translator.translate(12), "doze")
        self.assertEqual(translator.translate(15), "quinze")
        self.assertEqual(translator.translate(19), "dezenove")
        self.assertEqual(translator.translate(20), "vinte")
        self.assertEqual(translator.translate(30), "trinta")
        self.assertEqual(translator.translate(50), "cinquenta")
        self.assertEqual(translator.translate(90), "noventa")
        self.assertEqual(translator.translate(99), "noventa e nove")

    def test_translateReturnFullNumbers(self):
        self.assertEqual(translator.translate(-1042), "menos um mil e quarenta e dois")
        self.assertEqual(translator.translate(94587), "noventa e quatro mil e quinhentos e oitenta e sete")
        self.assertEqual(translator.translate(27100), "vinte e sete mil e cem")
        self.assertEqual(translator.translate(99101), "noventa e nove mil e cento e um")
        self.assertEqual(translator.translate(94587), "noventa e quatro mil e quinhentos e oitenta e sete")
        self.assertEqual(translator.translate(10010), "dez mil e dez")
        self.assertEqual(translator.translate(-10010), "menos dez mil e dez")
        self.assertEqual(translator.translate(94587), "noventa e quatro mil e quinhentos e oitenta e sete")


""" sem a função abaixo, use python -m unittest arquivo.py para rodar os testes"""
if __name__ == '__main__':
    unittest.main()
