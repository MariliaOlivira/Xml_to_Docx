import pygame
import random
import sys
# Inicializa o Pygame
pygame.init()

# Define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Cria as tartarugas
tartaruga1 = "Tartaruga 1"
tartaruga2 = "Tartaruga 2"

# Cria o placar
placar = {tartaruga1: 0, tartaruga2: 0}

# Estabelece o número de voltas que as tartarugas devem dar
num_voltas = 3

# Cria a janela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela
pygame.display.set_caption("Corrida de Tartarugas")

# Define o relógio do Pygame
relogio = pygame.time.Clock()

# Executa o jogo em loop infinito
while True:
    # Verifica os eventos do mouse e teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche a tela com uma cor sólida
    tela.fill(BRANCO)

    # Desenha as tartarugas
    pygame.draw.rect(tela, PRETO, (100, placar[tartaruga1], 50, 50))
    pygame.draw.rect(tela, PRETO, (600, placar[tartaruga2], 50, 50))

    # Desenha a pista
    pygame.draw.line(tela, PRETO, (0, 0), (0, altura_tela), 5)
    pygame.draw.line(tela, PRETO, (largura_tela - 5, 0),
                     (largura_tela - 5, altura_tela), 5)

    # Atualiza o placar
    fonte = pygame.font.Font(None, 36)
    placar_tartaruga1 = fonte.render(
        f"{tartaruga1}: {placar[tartaruga1]}", True, PRETO)
    placar_tartaruga2 = fonte.render(
        f"{tartaruga2}: {placar[tartaruga2]}", True, PRETO)
    tela.blit(placar_tartaruga1, (25, 25))
    tela.blit(placar_tartaruga2, (625, 25))

    # Atualiza a tela
    pygame.display
