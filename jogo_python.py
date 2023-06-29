import time,os,random
from perguntas import Perguntas



#Instancia objeto de perguntas
perguntas = Perguntas()
#Obtendo as perguntas
perguntas = perguntas.retorna_perguntas()

# Função para exibir uma pergunta e verificar a resposta
def fazer_pergunta(pergunta, resposta_correta, tempo_limite):
    print(pergunta)
    tempo_inicial = time.time()
    resposta = input("Digite sua resposta: ")
    tempo_final = time.time()

    tempo_decorrido = tempo_final - tempo_inicial

    if tempo_decorrido > tempo_limite:
        print('Tempo Esgotado! Você ultrapassou os 30 segundos de resposta')
        print('A resposta correta seria: ', resposta_correta)
        return False

    if resposta.lower() == resposta_correta.lower():
        print("Resposta correta!")
        return True
    else:
        print("Resposta incorreta!")
        print('A resposta correta seria: ', resposta_correta)
        return False

# Função para iniciar o jogo
def jogar_jogo():
    perguntas_feitas = []
    pontuacao = 0
    tempo_limite = 5  # Tempo limite para responder cada pergunta (em segundos)
    

    pergunta_testes = list(perguntas.keys())

    #embaralhaça as perguntas
    random.shuffle(pergunta_testes)
    contador = 0
    #percorre as perguntas embaralhadas
    for pergunta in pergunta_testes:
        resposta = perguntas[pergunta]

        #valida se a pergunta já foi feita antes
        if pergunta not in perguntas_feitas:
            
            if fazer_pergunta(pergunta, resposta, tempo_limite):
                pontuacao += 1
            else:
                pontuacao -= 1
                
            perguntas_feitas.append(pergunta)
        else:
            print(f"Pergunta: {pergunta} já feita antes")
            os.system('cls')

        os.system('cls')
        contador = contador + 1

        #Define quantas perguntas máxima pode
        if contador == 10:
            break

    print("\nFim do jogo!")
    print("Você acertou x perguntas:  e sua  Pontuação final: ", pontuacao)

        

# Iniciar o jogo
jogar_jogo()