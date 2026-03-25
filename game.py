import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
bird_pos = 300
tunnel_pos = 700

background = pygame.transform.scale(pygame.image.load("images/background.png"), screen.get_size())

bird_surface = pygame.image.load("images/bird.png").convert_alpha()
bird = pygame.transform.scale(bird_surface, (60,60))

tunnel_surface1 = pygame.image.load("images/tunnel1.png").convert_alpha()
tunnel1 = pygame.transform.scale(tunnel_surface1, (100,200))

tunnel_surface2 = pygame.image.load("images/tunnel2.png").convert_alpha()
tunnel2 = pygame.transform.scale(tunnel_surface2, (100,250))

game_over = pygame.font.SysFont("comicsansms", 50)
game_over_text = game_over.render("GAME OVER", True, 'Red')
game_over_rect = game_over_text.get_rect(center = (400 ,400))

def draw_background():
    screen.blit(background, (0,0))

def draw_bird(y_pos):
    bird_rect = bird.get_rect(topleft=(50, y_pos))
    screen.blit(bird, bird_rect)
    smaller_rect = bird_rect.inflate(-30, -30)
    return smaller_rect

def draw_tunnel1(x_pos):
    tunnel_rect = tunnel1.get_rect(topleft=(x_pos, 0))
    screen.blit(tunnel1, tunnel_rect)
    return tunnel_rect

def draw_tunnel2(x_pos):
    tunnel_rect = tunnel2.get_rect(bottomleft=(x_pos, 630))
    screen.blit(tunnel2, tunnel_rect)
    return tunnel_rect

def draw_game_over():
    screen.fill('Black')
    screen.blit(game_over_text, game_over_rect)

running = True
restart = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not restart:
            bird_pos -= 45
            if bird_pos <= 0:
                bird_pos = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart:
                restart = False
                bird_pos = 300
                tunnel_pos = 700
    draw_background()
    br = draw_bird(bird_pos)
    #pygame.draw.rect(screen, 'Green', br)
    tr1 = draw_tunnel1(tunnel_pos)
    #pygame.draw.rect(screen, 'Red', tr1)
    tr2 = draw_tunnel2(tunnel_pos)
    #pygame.draw.rect(screen, 'Red', tr2)
    ground_rect =pygame.Rect(0,620,800,170)
    if not restart:
        bird_pos += 1.3
        tunnel_pos -= 1.1
    if tunnel_pos < -100:
        tunnel_pos = 800
    if br.colliderect(ground_rect) or br.colliderect(tr1) or tr2.colliderect(br):
        draw_game_over()
        restart = True
    pygame.display.update()
    clock.tick(60)
pygame.quit()