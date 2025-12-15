import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.robo = configurar_robo()

        return super().setUpClass()
    
    def testar_01_oi_ola(self):
        self.assertIsNotNone(self.robo)

        saudacoes = ["oi", "olá", "tudo bem?", "como vai?"]
        for saudacao in saudacoes:
            resposta = self.robo.get_response(saudacao)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Olá, sou o seu AtendenteBot, um robô de suporte . O que você gostaria de saber ?".lower(), resposta.text.lower())

    def testar_02_bom_dia_tarde_noite(self):
        self.assertIsNotNone(self.robo)

        saudacoes = ["bom dia", "boa tarde", "boa noite"]
        for saudacao in saudacoes:
            resposta = self.robo.get_response(saudacao)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(f"{saudacao}, sou o seu AtendenteBot, um robô de suporte . O que você gostaria de saber ?" .lower(), resposta.text.lower())

    def testar_03_variabilidades(self):
        self.assertIsNotNone(self.robo)

        variabilidades = ["oi, tudo bem", "olá, como vai?", "ola, tudo bem?", "oi. como vai?"]

        for variabilidade in variabilidades:
            print(f"testando a variabilidade: {variabilidade}")

            resposta = self.robo.get_response(variabilidade)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Olá, sou o seu AtendenteBot, um robô de suporte . O que você gostaria de saber ?" .lower(), resposta.text.lower())
            
    def testar_04_Produtos(self):
        self.assertIsNotNone(self.robo)

        Pergunta = ["O que voces vendem?",
                "O que a empresa comercializa?",
                " quais são os seus produtos?"]
        for Pergunta in Pergunta:
            print(f"testando a pergunta: {Pergunta}")
            resposta = self.robo.get_response(Pergunta)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Nós temos Moveis, Eletrodomésticos, Eletrônicos, Informática e muito mais.".lower(), resposta.text.lower())
            
    def testar_05_Entrega(self):
        self.assertIsNotNone(self.robo)

        Perguntas = [ "Como funciona a entrega?","Vocês entregam?","Qual é o prazo de entrega?"]
        
        for Perguntas in Perguntas:
            print(f"testando a pergunta: {Perguntas}")
            resposta = self.robo.get_response(Perguntas)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("A entrega é feita em todo o território nacional, com prazos que variam conforme a região e o produto adquirido.".lower(), resposta.text.lower())
            
    def testar_06_Devolucao(self):
        self.assertIsNotNone(self.robo)

        duvida = [  "Como é a política de devolução?","Posso devolver um produto?","Qual é o processo de devolução?"]
        
        for duvida in duvida:
            print(f"testando a pergunta: {duvida}")
            resposta = self.robo.get_response(duvida)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Nossa política de devolução permite que você devolva produtos em até 30 dias após o recebimento, desde que estejam em condições originais.".lower(), resposta.text.lower())
    
    def testar_07_Garantia(self):
        self.assertIsNotNone(self.robo)

        Duvidas = [ "tem garantia nos produtos?",
                "Esses produtos têm garantia?",
                "tem garantia?"]
        for Duvidas in Duvidas:
            resposta = self.robo.get_response(Duvidas)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Todos os itens vêm com garantia do fabricante, que varia conforme o item adquirido."
        .lower(), resposta.text.lower())      
            
    def testar_08_Pagamento(self):
        self.assertIsNotNone(self.robo)

        duvidas = ["Quais são as formas de pagamento?","Como posso pagar pelos produtos?","Quais métodos de pagamento vocês aceitam?"]
        for duvidas in duvidas:
            resposta = self.robo.get_response(duvidas)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Aceitamos diversas formas de pagamento, incluindo cartões de crédito, débito, boleto bancário e transferências online."
        .lower(), resposta.text.lower())     
    
    def testar_09_localizacao(self):
        self.assertIsNotNone(self.robo)

        Interrogacao = ["Onde vocês estão localizados?",
                "Qual é o endereço da empresa?",
                "Onde fica a sede da empresa?"]
        for Interrogacao in Interrogacao:
            print(f"testando a pergunta: {Interrogacao}")
            resposta = self.robo.get_response(Interrogacao)

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Nossa sede está localizada na Av. Exemplo, 1234, Cidade, Estado, CEP 00000-000."
        .lower(), resposta.text.lower())
          

unittest.main()