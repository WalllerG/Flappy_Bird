import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
bird_pos = 300
tunnel_pos1 = 700
tunnel_pos2 = 1000
tunnel_pos3 = 1300
tunnel_pos4 = 1600
tunnels = []

background = pygame.transform.scale(pygame.image.load("images/background.png"), screen.get_size())

bird_surface = pygame.image.load("images/bird.png").convert_alpha()
bird = pygame.transform.scale(bird_surface, (60,60))

tunnel_surface1 = pygame.image.load("images/tunnel1.png").convert_alpha()
tunnel1 = pygame.transform.scale(tunnel_surface1, (100,200))
tunnel_surface2 = pygame.image.load("images/tunnel2.png").convert_alpha()
tunnel2 = pygame.transform.scale(tunnel_surface2, (100,250))

tunnel_surface3 = pygame.image.load("images/tunnel1.png").convert_alpha()
tunnel3 = pygame.transform.scale(tunnel_surface3, (100,240))
tunnel_surface4 = pygame.image.load("images/tunnel2.png").convert_alpha()
tunnel4 = pygame.transform.scale(tunnel_surface4, (100,280))

tunnel_surface5 = pygame.image.load("images/tunnel1.png").convert_alpha()
tunnel5 = pygame.transform.scale(tunnel_surface5, (100,150))
tunnel_surface6 = pygame.image.load("images/tunnel2.png").convert_alpha()
tunnel6 = pygame.transform.scale(tunnel_surface6, (100,350))

tunnel_surface7 = pygame.image.load("images/tunnel1.png").convert_alpha()
tunnel7 = pygame.transform.scale(tunnel_surface7, (100,300))
tunnel_surface8 = pygame.image.load("images/tunnel2.png").convert_alpha()
tunnel8 = pygame.transform.scale(tunnel_surface8, (100,200))



game_over = pygame.font.SysFont("comicsansms", 50)
game_over_text = game_over.render("GAME OVER", True, 'Red')
game_over_rect = game_over_text.get_rect(center = (400 ,400))

def draw_background():
    screen.blit(background, (0,0))

def draw_bird(y_pos):
    bird_rect = bird.get_rect(topleft=(150, y_pos))
    screen.blit(bird, bird_rect)
    smaller_rect = bird_rect.inflate(-30, -30)
    return smaller_rect

def draw_tunnel1(x_pos):
    tunnel_rect1 = tunnel1.get_rect(topleft=(x_pos, 0))
    screen.blit(tunnel1, tunnel_rect1)
    tunnel_rect2 = tunnel2.get_rect(bottomleft=(x_pos, 630))
    screen.blit(tunnel2, tunnel_rect2)
    return tunnel_rect1, tunnel_rect2

def draw_tunnel2(x_pos):
    tunnel_rect3 = tunnel3.get_rect(topleft=(x_pos, 0))
    screen.blit(tunnel3, tunnel_rect3)
    tunnel_rect4 = tunnel4.get_rect(bottomleft=(x_pos, 630))
    screen.blit(tunnel4, tunnel_rect4)
    return tunnel_rect3, tunnel_rect4

def draw_tunnel3(x_pos):
    tunnel_rect5 = tunnel5.get_rect(topleft=(x_pos, 0))
    screen.blit(tunnel5, tunnel_rect5)
    tunnel_rect6 = tunnel6.get_rect(bottomleft=(x_pos, 630))
    screen.blit(tunnel6, tunnel_rect6)
    return tunnel_rect5, tunnel_rect6

def draw_tunnel4(x_pos):
    tunnel_rect7 = tunnel7.get_rect(topleft=(x_pos, 0))
    screen.blit(tunnel7, tunnel_rect7)
    tunnel_rect8 = tunnel8.get_rect(bottomleft=(x_pos, 630))
    screen.blit(tunnel8, tunnel_rect8)
    return tunnel_rect7, tunnel_rect8

def draw_game_over():
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
                tunnel_pos1 = 700
                tunnel_pos2 = 1000
                tunnel_pos3 = 1300
                tunnel_pos4 = 1600
    draw_background()
    br = draw_bird(bird_pos)
    tr1, tr2 = draw_tunnel1(tunnel_pos1)
    tr3, tr4 = draw_tunnel2(tunnel_pos2)
    tr5, tr6 = draw_tunnel3(tunnel_pos3)
    tr7, tr8 = draw_tunnel4(tunnel_pos4)
    ground_rect =pygame.Rect(0,620,800,170)
    if not restart:
        bird_pos += 2.5
        tunnel_pos1 -= 4
        tunnel_pos2 -= 4
        tunnel_pos3 -= 4
        tunnel_pos4 -= 4
        if tunnel_pos1 < -100:
            tunnel_pos1 = tunnel_pos4 + 300
        if tunnel_pos2 < -100:
            tunnel_pos2 = tunnel_pos1 + 300
        if tunnel_pos3 < -100:
            tunnel_pos3 = tunnel_pos2 + 300
        if tunnel_pos4 < -100:
            tunnel_pos4 = tunnel_pos3 + 300
        if br.colliderect(ground_rect) or br.colliderect(tr1) or br.colliderect(tr2) or br.colliderect(tr3) or br.colliderect(tr4) or br.colliderect(tr5) or br.colliderect(tr6) or br.colliderect(tr7) or br.colliderect(tr8):
            restart = True
    if restart:
        draw_game_over()
    pygame.display.update()
    clock.tick(60)
pygame.quit()