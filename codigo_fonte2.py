import pygame
import sys
import funcoes
import time
from pygame.locals import*

pygame.init()
x = 800
y = 600
tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("Snake Beta")
grafico = funcoes.grafica()

# variaveis
fase = 0
opcao_menu = 0
orientacao = 0
comidinha = (200, 200)
pontuacao = 0
corpo = []
som = pygame.mixer.Sound("ben.ogg")
som.set_volume(0.4)

# ciclo do jogo
while True:
    if fase == 0:
        grafico.fundo()
        grafico.titulo(opcao_menu)

    elif fase == 1:
        time.sleep(0.09)
        grafico.fundo()
        grafico.limite()
        comidinha, pontuacao = grafico.cobra(orientacao, comidinha, pontuacao)
        grafico.comida(comidinha)
        grafico.placar(pontuacao)
        pass
    elif fase == 2:
        som.play()
        grafico.fundo()
        grafico.sobre()
        pass
    # corpo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pass
        elif evento.type == KEYDOWN:
            if fase == 0:
                if evento.key == pygame. K_DOWN:
                    if opcao_menu < 1:
                        opcao_menu += 1
                    else:
                        opcao_menu = 0
                elif evento.key == pygame.K_UP:
                    if opcao_menu > 0:
                        opcao_menu -= 1
                    else:
                        opcao_menu = 1
                elif evento.key == pygame.K_RETURN:
                    if opcao_menu == 0:
                        fase = 1
                    elif opcao_menu == 1:
                        fase = 2
            elif fase == 1:
                if evento.key == pygame.K_DOWN and orientacao != 90:
                    orientacao = 270
                if evento.key == pygame.K_UP and orientacao != 270:
                    orientacao = 90
                if evento.key == pygame.K_LEFT and orientacao != 0:
                    orientacao = 180
                if evento.key == pygame.K_RIGHT and orientacao != 180:
                    orientacao = 0
                if evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_m:
                    fase = 0
            elif fase == 2:
                if evento.key == pygame.K_ESCAPE:
                    som.stop()
                    fase = 0
        elif evento.type == KEYUP:
            pass

    pygame.display.update()
    pass