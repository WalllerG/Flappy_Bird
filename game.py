import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
bird_pos = 300
bird_velocity = 0
gravity = 0.2
jump_strength = -3.5
GAP_SIZE = 150
tunnel_pos1 = 700
tunnel_pos2 = 1000
tunnel_pos3 = 1300
tunnel_pos4 = 1600
gap1 = random.randint(200, 400)
gap2 = random.randint(200, 400)
gap3 = random.randint(200, 400)
gap4 = random.randint(200, 400)

background = pygame.transform.scale(pygame.image.load("images/background.png"), screen.get_size())

bird_surface = pygame.image.load("images/bird.png").convert_alpha()
bird = pygame.transform.scale(bird_surface, (60,60))

top_tunnel_img = pygame.image.load("images/tunnel1.png").convert_alpha()
bot_tunnel_img = pygame.image.load("images/tunnel2.png").convert_alpha()

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

def draw_tunnels(x_pos, gap_y):
    top_height = gap_y - (GAP_SIZE // 2)
    bottom_height = 630 - (gap_y + (GAP_SIZE // 2))
    scaled_top = pygame.transform.scale(top_tunnel_img, (100, top_height))
    scaled_bottom = pygame.transform.scale(bot_tunnel_img, (100, bottom_height))
    top_rect = scaled_top.get_rect(topleft=(x_pos, 0))
    bottom_rect = scaled_bottom.get_rect(bottomleft=(x_pos, 630))
    screen.blit(scaled_top, top_rect)
    screen.blit(scaled_bottom, bottom_rect)

    return top_rect, bottom_rect

def draw_game_over():
    screen.blit(game_over_text, game_over_rect)

running = True
restart = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN     :
            bird_velocity = jump_strength
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
    tr1, tr2 = draw_tunnels(tunnel_pos1, gap1)
    tr3, tr4 = draw_tunnels(tunnel_pos2, gap2)
    tr5, tr6 = draw_tunnels(tunnel_pos3, gap3)
    tr7, tr8 = draw_tunnels(tunnel_pos4, gap4)
    ground_rect =pygame.Rect(0,620,800,170)
    if not restart:
        bird_velocity += gravity
        bird_pos += bird_velocity
        tunnel_pos1 -= 4
        tunnel_pos2 -= 4
        tunnel_pos3 -= 4
        tunnel_pos4 -= 4
        if bird_pos <= 0:
            bird_pos = 0
            bird_velocity = 0
        if tunnel_pos1 < -100:
            tunnel_pos1 = tunnel_pos4 + 300
            gap1 = random.randint(200, 400)
        if tunnel_pos2 < -100:
            tunnel_pos2 = tunnel_pos1 + 300
            gap2 = random.randint(200, 400)
        if tunnel_pos3 < -100:
            tunnel_pos3 = tunnel_pos2 + 300
            gap3 = random.randint(200, 400)
        if tunnel_pos4 < -100:
            tunnel_pos4 = tunnel_pos3 + 300
            gap4 = random.randint(200, 400)
        if br.colliderect(ground_rect) or br.colliderect(tr1) or br.colliderect(tr2) or br.colliderect(tr3) or br.colliderect(tr4) or br.colliderect(tr5) or br.colliderect(tr6) or br.colliderect(tr7) or br.colliderect(tr8):
            restart = True
    if restart:
        draw_game_over()
    pygame.display.update()
    clock.tick(60)
pygame.quit()