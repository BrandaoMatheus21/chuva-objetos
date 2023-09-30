import pygame 
from sys import exit
from random import randint, choice

def adicionar_objeto():
    global lista_chuva_objetos

    objetos_lista_aleatoria = ['coracao'] * 10 + ['moeda'] * 10 + ['projetil'] * 80
    tipo_objeto = choice(objetos_lista_aleatoria)

    posicao = (randint(10, 950)), randint(-100, 0)
    velocidade = randint(5, 10)

    if tipo_objeto == 'projetil':
        objeto_rect = projetil_superficies[0].get_rect(center=posicao)
    elif tipo_objeto == 'coracao':
        objeto_rect = coracao_superficies[0].get_rect(center=posicao)
    elif tipo_objeto == 'moeda':
        objeto_rect = moeda_superficies[0].get_rect(center=posicao)



    objeto_rect = projetil_superficies[0].get_rect(center=posicao)

    lista_chuva_objetos.append({
        'tipo': tipo_objeto,
        'retangulo': objeto_rect,
        'velocidade': velocidade
    })

def movimento_objetos_chuva():
    global lista_chuva_objetos

    for objeto in lista_chuva_objetos:

        objeto['retangulo'].y += objeto['velocidade']

        if objeto['tipo'] == 'projetil':
            tela.blit(projetil_superficies[projetil_index], objeto['retangulo'])
        if objeto['tipo'] == 'coracao':
            tela.blit(coracao_superficies[projetil_index], objeto['retangulo'])
        if objeto['tipo'] == 'moeda':
            tela.blit(moeda_superficies[projetil_index], objeto['retangulo'])
        if objeto['retangulo'].y > 540:
            lista_chuva_objetos.remove(objeto)

def animacao_personagem():
    global jogador_index
        # Calcula o movimento do personagem
    jogador_parado_rect.x += movimento_personagem

    if movimento_personagem == 0: #Jogador parado
        jogador_superficies = jogador_parado_superficies
    else: #Jogador andando
        jogador_superficies = jogador_voando_superficies
    
    #avança para proximo frame
    jogador_index += 0.09
    if jogador_index >len(jogador_superficies) -1:
        jogador_index = 0
 
    if direcao_personagem == 1:
        jogador = pygame.transform.flip(jogador_superficies[int(jogador_index)], True, False) 
    else:
        jogador = jogador_superficies[int(jogador_index)]

    # Coloca o jogador na tela
    tela.blit(jogador_superficies[int(jogador_index)], jogador_parado_rect)

    jogador_index += 0.09

    if jogador_index > len(jogador_superficies) -1:
        jogador_index = 0

# Inicializa o pygame 
pygame.init()

# Cria a tela 
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

## Importa os arquivos necessarios

# Carrega o plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background1.png').convert()
plano_fundo2 = pygame.image.load('assets/fundo/Night-Background2.png').convert()
plano_fundo3 = pygame.image.load('assets/fundo/Night-Background3.png').convert()
plano_fundo4= pygame.image.load('assets/fundo/Night-Background4.png').convert()
plano_fundo5= pygame.image.load('assets/fundo/Night-Background5.png').convert()
plano_fundo6 = pygame.image.load('assets/fundo/Night-Background6.png').convert()
plano_fundo7 = pygame.image.load('assets/fundo/Night-Background7.png').convert()
plano_fundo8 = pygame.image.load('assets/fundo/Night-Background8.png').convert()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
plano_fundo2 = pygame.transform.scale(plano_fundo2, tamanho)
plano_fundo3 = pygame.transform.scale(plano_fundo3, tamanho)
plano_fundo4 = pygame.transform.scale(plano_fundo4, tamanho)
plano_fundo5 = pygame.transform.scale(plano_fundo5, tamanho)
plano_fundo6 = pygame.transform.scale(plano_fundo6, tamanho)
plano_fundo7 = pygame.transform.scale(plano_fundo7, tamanho)
plano_fundo8 = pygame.transform.scale(plano_fundo8, tamanho)

# Carrega as imagens do personagem
jogador_index = 0 
jogador_parado_superficies = []
jogador_voando_superficies = []

for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_superficies.append(img)

# Carrega as imagens do personagem voando

for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_superficies.append(img)

jogador_parado_rect = jogador_parado_superficies[jogador_index].get_rect( center = (100, 430))

# Carrega o coração
coracao_superficies = []
coracao_index = 0
for imagem in range(1, 4):
    img = pygame.image.load(f'assets/objetos/coracao/Heart{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    coracao_superficies.append(img)

# Carrrega a moeda
moeda_index = 0
moeda_superficies = []
for imagem in range(1, 5):
    img = pygame.image.load(f'assets/objetos/moeda/Coin-A{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    moeda_superficies.append(img)

#Carrega o projetil
projetil_index = 0
projetil_superficies = []
for imagem in range(1, 4):
    img = pygame.image.load(f'assets/objetos/projetil/Hero Bullet{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80, 80))
    projetil_superficies.append(img)
   
# Guardar os objetos que vao cair
lista_chuva_objetos = []

# Define o titulo da janela
pygame.display.set_caption("ChuvaMortal")        

# Cria um relógio para controlar os FPS
relogio = pygame.time.Clock()

# Controla se o personagem está andando (negativo esquerda, positivo direita)
movimento_personagem = 0
direcao_personagem = 0

# Cria um evento para adicionar na tela um objeto
novo_objeto_timer = pygame.USEREVENT + 1
pygame.time.set_timer(novo_objeto_timer, 500)

# Loop principal do jogo
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
            
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0
            
            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0
            
        if evento.type == novo_objeto_timer:
            adicionar_objeto()

    # Coloca imagem na tela
    tela.blit(plano_fundo8, (0, 0))
    tela.blit(plano_fundo7, (0, 0))
    tela.blit(plano_fundo6, (0, 0))
    tela.blit(plano_fundo5, (0, 0))
    tela.blit(plano_fundo4, (0, 0))
    tela.blit(plano_fundo3, (0, 0))
    tela.blit(plano_fundo2, (0, 0))
    tela.blit(plano_fundo, (0, 0))

    # Faz a chamada da função animação do personagem
    animacao_personagem()

    #Animação objetos chuva
    movimento_objetos_chuva()

    # Chuva de objetos
    adicionar_objeto()

    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)
