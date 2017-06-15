import pygame
import sys
import funcoes
import time
from pygame.locals import*

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Beta (base fonte)")
grafico = funcoes.grafica()

# variaveis
fase = 0
opcao_menu = 0
orientacao = 0


# ciclo do jogo
while True:
    if fase == 0:
        grafico.fundo()
        grafico.titulo(opcao_menu)
    elif fase == 1:
        grafico.fundo()
        grafico.cobra(orientacao)
        pass
    elif fase == 2:
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
                elif evento.key == pygame.K_s:
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
            elif fase == 2:
                if evento.key == pygame.K_v:
                    fase = 0
        elif evento.type == KEYUP:
            pass

    pygame.display.update()
    time.sleep(0.09)
    pass
