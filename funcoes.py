import pygame
import random
from pygame.locals import*
pygame.init()

x = 800
y = 600

janela = pygame.display.set_mode((x, y))
fundo_verde = (4, 166, 1)                  # cor do fundo da tela
cor_letra = (0, 0, 0)               # cor da letra
cor_cursor = (50, 60, 50)
cor_cobra = (255, 55, 255)
red = (255, 0, 0)

# snake
corpo = [(80, 80), (80, 100)]   # cria um vetor, entre os parênteses estão as posições tupla
cabeca = corpo

# sons do jogo
som2 = pygame.mixer.Sound("pin.ogg")
som2.set_volume(0.7)


# fonte de texto
fonte_titulo = pygame.font.SysFont("Noto Sans CJK JP Black", 50)
fonte_menu = pygame.font.SysFont("Verdana", 25)
fonte_texto = pygame.font.SysFont("Times New Roman", 15)
fonte_sobre = pygame.font.SysFont("Times New Roman", 25)

# textos que aparecerão na tela
titulo = fonte_titulo.render("Snake", True, (cor_letra))
game_over = fonte_titulo.render("Você morreu", True, (cor_letra))
game_over1 = fonte_titulo.render("Pressione 'q' para sair", True, (cor_letra))
game_over2 = fonte_titulo.render("Pressione 'm' para voltar ao menu", True, (cor_letra))
jogador = fonte_menu.render("Jogar", True, (cor_letra))
sobre = fonte_menu.render("Sobre", True, (cor_letra))
instrucao = fonte_texto.render("Pressione 'ENTER' para selecionar uma opção", True, (cor_letra))
instrucao2 = fonte_texto.render("Pressione 'ESC' para voltar", True, (cor_letra))
sobre1 = fonte_sobre.render("*Desenvolvedores:", True, (cor_letra))
sobre2 = fonte_sobre.render("Nayara Cerdeira", True, (cor_letra))
sobre3 = fonte_sobre.render("Enrique Izel", True, (cor_letra))
sobre4 = fonte_sobre.render("*Orientador:", True, (cor_letra))
sobre5 = fonte_sobre.render("Dr Jucimar Jr", True, (cor_letra))
sobre6 = fonte_sobre.render("Músicas usadas:", True, (cor_letra))
sobre7 = fonte_sobre.render("Rubel - Ben", True, (cor_letra))
sobre8 = fonte_sobre.render("Universidade do Estado do Amazonas", True, (cor_letra))
placar = fonte_sobre.render("Score: ", True, (cor_letra))

class grafica():
    def __init__(self):
        print("Novos graficos")
        pass
    def fundo(self):
        janela.fill(fundo_verde)

    def titulo(self, opcoes):   # "opcao" é a sombra do cursor que indica o que o usuário selecionará
        if opcoes == 0:
            pygame.draw.rect(janela, cor_cursor, (110, 200, 300, 30))
        elif opcoes == 1:
            pygame.draw.rect(janela, cor_cursor, (110, 230, 300, 30))
        janela.blit(titulo, (80, 50))
        janela.blit(jogador, (120, 200))
        janela.blit(sobre, (120, 230))
        janela.blit(instrucao, (10, 550))
        pass
    def sobre(self):
        janela.blit(sobre, (350, 50))
        janela.blit(sobre1, (20, 60))
        janela.blit(sobre3, (50, 100))
        janela.blit(sobre2, (50, 150))
        janela.blit(sobre4, (20, 200))
        janela.blit(sobre5, (50, 250))
        janela.blit(sobre6, (500, 60))
        janela.blit(sobre7, (500, 100))
        janela.blit(sobre8, (190, 10))
        janela.blit(instrucao2, (10, 550))

    def cobra(self, orientacao, comidinha, pontuacao):
        for i in corpo:
            jiboia = pygame.draw.rect(janela, cor_cobra, (i[0]+1, i[1]+1, 18, 18))
            print(jiboia.x, jiboia.y)
            if jiboia.y > 570:                     # baixo
                janela.blit(game_over, (150, 100))
                janela.blit(game_over1, (150, 250))
                janela.blit(game_over2, (150, 300))
                return (comidinha, pontuacao)
                print('bateu na borda e morreu')
            elif jiboia.x > 770.00:                  # da direita
                print('bateu na borda e morreu')
                janela.blit(game_over, (150,100))
                janela.blit(game_over1, (150,250))
                janela.blit(game_over2, (150,300))
                return (comidinha, pontuacao)
            elif jiboia.y == 1.00:                   # cima
                janela.blit(game_over, (150, 100))
                janela.blit(game_over1, (150, 250))
                janela.blit(game_over2, (150, 300))
                print('bateu na borda e morreu')
                return (comidinha, pontuacao)
            elif jiboia.x == 1.00:                   # esquerda
                janela.blit(game_over, (150, 100))
                janela.blit(game_over, (150, 250))
                janela.blit(game_over, (150, 300))
                print('bateu na borda e morreu')
                return (comidinha, pontuacao)
            elif cabeca.count(corpo) != 0:
                print("morreu")
                break
                return (comidinha, pontuacao, cabeca)
            if corpo.index(i) == len(corpo)-1:
                if orientacao == 0:
                    corpo.append((i[0] + 20, i[1]))
                if orientacao == 90:
                    corpo.append((i[0], i[1]-20))
                if orientacao == 270:
                    corpo.append((i[0], i[1]+20))
                if orientacao == 180:
                    corpo.append((i[0] - 20, i[1]))
                if i != comidinha:
                    del corpo[0]
                    return (comidinha, pontuacao)
                    #break
                else:
                    pontuacao += 1
                    som2.play()
                    return ((random.randint(0, 39)*20, random.randint(0, 29)*20), pontuacao)
                #break

    def comida(self, comidinha):
        pygame.draw.rect(janela, cor_cursor, (comidinha[0], comidinha[1], 18, 18))

    def placar(self, pontuacao):
        janela.blit(placar, (0, 0))
        pontos = fonte_sobre.render(str(pontuacao), True, cor_letra)
        janela.blit(pontos, (80, 0))

    def limite(self):
        pygame.draw.rect(janela, red, [0, 0, 800, 0])
        pygame.draw.rect(janela, red, [0, 0, 0, 600])
        pygame.draw.rect(janela, red, [0, 600, 800, 0])
        pygame.draw.rect(janela, red, [800, 0, 0, 800])
