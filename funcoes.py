import pygame
import random
from pygame.locals import*
pygame.init()

janela = pygame.display.set_mode((800, 600))
fundo_verde = (0, 255, 0)                  # cor do fundo da tela
cor_letra = (0, 0, 255)               # cor da letra
cor_cursor = (50, 60, 50)
cor_cobra = (0, 0, 0)

# snake
opcao = [(80, 80), (80, 100)]


# fonte de texto
fonte_titulo = pygame.font.SysFont("Arial", 50)
fonte_menu = pygame.font.SysFont("Verdana", 25)
fonte_texto = pygame.font.SysFont("Times New Roman", 15)
fonte_sobre = pygame.font.SysFont("Times New Roman", 25)

# textos que aparecerão na tela
titulo = fonte_titulo.render("Snake", True, (cor_letra))
jogador = fonte_menu.render("Jogar", True, (cor_letra))
sobre = fonte_menu.render("Sobre", True, (cor_letra))
instrucao = fonte_texto.render("Pressione 's' para selecionar uma opção", True, (cor_letra))
instrucao2 = fonte_texto.render("Pressione 'v' para voltar", True, (cor_letra))
sobre1 = fonte_sobre.render("*Desenvolvedores:", True, (cor_letra))
sobre2 = fonte_sobre.render("Nayara Cerdeira", True, (cor_letra))
sobre3 = fonte_sobre.render("Enrique Izel", True, (cor_letra))
sobre4 = fonte_sobre.render("*Orientador:", True, (cor_letra))
sobre5 = fonte_sobre.render("Dr Jucimar Jr", True, (cor_letra))
placar = fonte_sobre.render("Score: ", True, (cor_letra))

class grafica(object):
    def __init__(self):
        print("Novos graficos")
        pass
    def fundo(self):
        janela.fill(fundo_verde)

    def titulo(self, opcoes):   # "opcao" é a sombra deo cursor que indica o que o usuário selecionará
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
        janela.blit(sobre, (20, 20))
        janela.blit(sobre1, (20, 60))
        janela.blit(sobre2, (50, 150))
        janela.blit(sobre3, (50, 200))
        janela.blit(sobre4, (20, 300))
        janela.blit(sobre5, (50, 400))
        janela.blit(instrucao2, (10, 550))

    def cobra(self, orientacao, comidinha, pontuacao):
        for i in opcao:
            pygame.draw.rect(janela,cor_cobra, (i[0]+1, i[1]+1, 18 , 18))
            if opcao.index(i) == len(opcao)-1:
                if orientacao == 0:
                    opcao.append((i[0] + 20, i[1]))
                if orientacao == 90:
                    opcao.append((i[0],i[1]-20))
                if orientacao == 270:
                    opcao.append((i[0], i[1]+20))
                if orientacao == 180:
                    opcao.append((i[0] - 20, i[1]))
                if i != comidinha:
                    del opcao[0]
                    return (comidinha, pontuacao)
                else:
                    pontuacao += 1
                    return ((random.randint(0, 39)*20, random.randint(0, 29)*20), pontuacao)
                break

    def comida(self, comidinha):
        pygame.draw.rect(janela, cor_cursor, (comidinha[0], comidinha[1], 18, 18))
    def placar(self, pontuacao):
        janela.blit(placar, (10, 10))
        pontos = fonte_texto.render(str(pontuacao), True, cor_letra)
        janela.blit(pontos, (100, 10))