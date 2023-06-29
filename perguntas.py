
class Perguntas:

    def __init__(self) -> None:
        self.perguntas = {
            'Qual é a vegetação mais desmatada do Brasil?': 'Mata Atlântica',
            'Qual é a cor da lata do lixo orgânico?' : 'Marrom',
            'Qual é o gás mais poluente?' : 'Mónoxido de carbono',
            'Em qual cor da lixeira devemos descartar os metais?' : 'Amarelo',
            'Como devemos transportar nossa compra do supermercado?' : 'Usando caixas ou sacolas reutilizaveis',
            'O que causa a chuva ácida?' : 'Poluição do ar',
            'Atualmente qual país é o maior emissor de dióxido de carbono(CO2) ?' : 'China',
            'A maior parte do planeta é recoberto de?' : 'Água',
            'Nas lixeiras de coleta seletiva, a quais tipos de materiais correspondem as cores: verde, vermelho, amarelo e azul?' : 'Vidro, plástico, metal e papel',
            'Na hora de enfrentar a pilha de louça suja, o que gasta menos água?\nUsar a lava-louças ou lavar a louça na pia: ' : 'Usar a lava-louças',
            'Segundo a ONU, qual o consumo diário médio de água necessário por pessoa? (Em litros)' : '110',
            'O material que se decompõe mais rápido na natureza é:\nA) O papel B) O tecido C) O metal D) A madeira' : 'A',
            'Qual dessas atitudes não é sustentável?:\nA) Jogar óleo na pia B) Lavar o quintal com balde C) Reaproveitar a água da chuva' : 'A',
            'Qual desses materiais demora mais tempo para se decompor na natureza?:\nA) Restos de alimentos B) Vidro C) Fralda descartável D) Lata de Refrigerante' : 'B',
            'Qual desses itens não pode ser reciclado?:\nA) Tampinha de garrafa B) Jornal usado C) Guardanapo de papel usado D) Balde usado' : 'C',
            'O que podemos fazer para economizar mais energia elétrica?:\nA) Deixar a porta da geladeira aberta B) Tomar banhos demorados C) Apagar a luz ao sair dos ambientes onde não tem mais ninguém' : 'C',
            'Uma pessoa consumista é aquela que:\nA) Comprar somente o que precisa B) Compra coisas além do necessário C) Evitar fazer compras' : 'B', 
            'Entre as alternativas o único produto que pode ser reciclado é:\nA) Uma fotografia B) Um adesivo C) Um óculos D) Um prego' : 'D',
            'Podemos reaproveitar alimentos, como por exemplo, cascas de laranja, que só não servem para fazer:\nA) Doce em calda B) Suco C) Chá D) Adubo para plantas' : 'B'
            
            ,

        }
         

    def retorna_perguntas(self):

        #returna as perguntas o jogo
        
         return self.perguntas