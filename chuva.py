import pygame 
from sys import exit

#Inicializa o pygame 
pygame.init()

#Cria a tela 
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

##Importa os arquivos necessarios

#Carrega o plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background1.png').convert()
plano_fundo2 = pygame.image.load('assets/fundo/Night-Background2.png').convert()
plano_fundo3 = pygame.image.load('assets/fundo/Night-Background3.png').convert()
plano_fundo4= pygame.image.load('assets/fundo/Night-Background4.png').convert()
plano_fundo5= pygame.image.load('assets/fundo/Night-Background5.png').convert()
plano_fundo6 = pygame.image.load('assets/fundo/Night-Background6.png').convert()
plano_fundo7 = pygame.image.load('assets/fundo/Night-Background7.png').convert()
plano_fundo8 = pygame.image.load('assets/fundo/Night-Background8.png').convert()

#Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
plano_fundo2 = pygame.transform.scale(plano_fundo2, tamanho)
plano_fundo3 = pygame.transform.scale(plano_fundo3, tamanho)
plano_fundo4 = pygame.transform.scale(plano_fundo4, tamanho)
plano_fundo5 = pygame.transform.scale(plano_fundo5, tamanho)
plano_fundo6 = pygame.transform.scale(plano_fundo6, tamanho)
plano_fundo7 = pygame.transform.scale(plano_fundo7, tamanho)
plano_fundo8 = pygame.transform.scale(plano_fundo8, tamanho)

#Importa o personagem 
jogador_parado_surf = pygame.image.load('assets/jogador/parado/Hero Boy Idle1.png')
jogador_parado_rect = jogador_parado_surf.get_rect(midbottom = (100, 530))

#Define o titulo da janela
pygame.display.set_caption("ChuvaMortal")

#Cria um relógio para controlar os FPS
relogio = pygame.time.Clock()

movimento_personagem = 0
#Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5

            if evento.key == pygame.K_LEFT:
                movimento_personagem = -5

    #Coloca imagem na tela
    tela.blit(plano_fundo8, (0, 0))
    tela.blit(plano_fundo7, (0, 0))
    tela.blit(plano_fundo6, (0, 0))
    tela.blit(plano_fundo5, (0, 0))
    tela.blit(plano_fundo4, (0, 0))
    tela.blit(plano_fundo3, (0, 0))
    tela.blit(plano_fundo2, (0, 0))
    tela.blit(plano_fundo, (0, 0))

    #Coloca o jogador na tela
    jogador_parado_rect.x += movimento_personagem
    tela.blit(jogador_parado_surf, jogador_parado_rect)

    #Atualiza a tela com o conteudo
    pygame.display.update()

    #Define a quantidade de frames por segundo
    relogio.tick(60)
