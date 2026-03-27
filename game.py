import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
scroll = 0
scroll_speed = 2
bird_pos = 300
bird_velocity = 0
gravity = 0.2
jump_strength = -3.5
GAP_SIZE = 130
tunnel_pos1 = 700
tunnel_pos2 = 1000
tunnel_pos3 = 1300
tunnel_pos4 = 1600
gap1 = random.randint(200, 400)
gap2 = random.randint(200, 400)
gap3 = random.randint(200, 400)
gap4 = random.randint(200, 400)
COLOR_SHADOW = (180, 100, 40)
COLOR_OUTLINE = (255, 255, 255)
score = 0
crash_time = 0
pass1 = False
pass2 = False
pass3 = False
pass4 = False
restart_button = None
falling = False
waiting = False

starting_page_text = pygame.font.Font('game_font.ttf', 100)
starting_page_surf = starting_page_text.render("FlappyBird", True, 'White')
starting_page_rect = starting_page_surf.get_rect(center=(400,200))
starting_page_outline = starting_page_text.render("FlappyBird", True, 'Black')
starting_button_font = pygame.font.Font('game_font.ttf', 50)

background = pygame.transform.scale(pygame.image.load("images/background.png").convert_alpha(), screen.get_size())

bird_surface = pygame.image.load("images/bird.png").convert_alpha()
bird = pygame.transform.scale(bird_surface, (60,60))

top_tunnel_img = pygame.image.load("images/tunnel1.png").convert_alpha()
bot_tunnel_img = pygame.image.load("images/tunnel2.png").convert_alpha()

score_surf = pygame.font.Font('score_font.ttf', 66)

game_over = pygame.font.Font('game_font.ttf', 80)
game_over_text = game_over.render("GAME OVER", True, (245, 160, 80))
game_over_rect = game_over_text.get_rect(center=(400, 230))

def draw_starting_page(pos):
    screen.blit(background, (pos, 0))
    screen.blit(background, (pos + background.get_width(), 0))
    for ox, oy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, -3), (0, 3), (-3, 0), (3, 0)]:
        screen.blit(starting_page_outline, (starting_page_rect.topleft[0] + ox, starting_page_rect.topleft[1] + oy))
    screen.blit(starting_page_surf, starting_page_rect)
    new_bird = pygame.transform.scale(bird_surface, (100, 100))
    bird_rect = new_bird.get_rect(center=(starting_page_rect.center[0]-10,starting_page_rect.center[1] + 150))
    screen.blit(new_bird, bird_rect)
    starting_button = starting_button_font.render("START", True, 'Darkgreen')
    starting_button_rect = starting_button.get_rect(center = (starting_page_rect.center[0],starting_page_rect.center[1] + 300))
    start_button_frame = starting_button_rect.inflate(100,40)
    frame_outline = start_button_frame.inflate(1,1)
    pygame.draw.rect(screen, 'White', start_button_frame, 0, 20)
    pygame.draw.rect(screen, 'Black', frame_outline, 3, 20)
    screen.blit(starting_button, starting_button_rect)
    return frame_outline

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
    bottom_rect = scaled_bottom.get_rect(bottomleft=(x_pos, 625))
    screen.blit(scaled_top, top_rect)
    screen.blit(scaled_bottom, bottom_rect)
    return top_rect, bottom_rect

def draw_game_over():
    screen.fill('LightGreen')
    outline_surf = game_over.render("GAME OVER", True, COLOR_OUTLINE)
    for ox, oy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, -2), (0, 2), (-2, 0), (2, 0)]:
        screen.blit(outline_surf, (game_over_rect.topleft[0] + ox, game_over_rect.topleft[1] + oy))
    shadow_surf = game_over.render("GAME OVER", True, COLOR_SHADOW)
    screen.blit(shadow_surf, (game_over_rect.topleft[0], game_over_rect.topleft[1] + 4))
    screen.blit(game_over_text, game_over_rect)
    score_text = game_over.render(f"SCORE: {score}", True, '#9A6735')
    score_rect = score_text.get_rect(topleft=(game_over_rect.topleft[0] + 30, game_over_rect.topleft[1] + 120))
    score_outline = game_over.render(f"SCORE: {score}", True, 'White')
    for ox, oy in [(-2, -2), (2, -2), (-2, 2), (2, 2), (0, -2), (0, 2), (-2, 0), (2, 0)]:
        screen.blit(score_outline, (score_rect.topleft[0] + ox, score_rect.topleft[1] + oy))
    screen.blit(score_text, score_rect)
    restart_font = pygame.font.Font('score_font.ttf', 40)
    restart_text = restart_font.render("RESTART", True, 'White')
    restart_rect = restart_text.get_rect(center=(game_over_rect.centerx, game_over_rect.centery + 220))
    restart_frame_rect = restart_rect.inflate(12, 12)
    outline_rect = restart_frame_rect.inflate(1, 1)
    pygame.draw.rect(screen,'#9A6735', restart_frame_rect, 0, 10)
    pygame.draw.rect(screen,'Black', outline_rect, 2, 10)
    screen.blit(restart_text, restart_rect)
    return outline_rect

def draw_score():
    score_text = score_surf.render(str(score), True, 'White')
    score_rect = score_text.get_rect(midtop=(400, 0))
    outline_surf = score_surf.render(str(score), True, 'Black')
    for ox, oy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, -3), (0, 3), (-3, 0), (3, 0)]:
        screen.blit(outline_surf, (score_rect.topleft[0] + ox, score_rect.topleft[1] + oy))
    screen.blit(score_text, score_rect)

running = True
restart = False
game_active = False
start_game = None

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not falling:
            bird_velocity = jump_strength
        if restart:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    waiting = False
                    falling = False
                    restart_button = None
                    restart = False
                    bird_pos = 300
                    bird_velocity = 0
                    tunnel_pos1 = 700
                    tunnel_pos2 = 1000
                    tunnel_pos3 = 1300
                    tunnel_pos4 = 1600
                    score = 0
        if not game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.collidepoint(event.pos):
                    game_active = True
    if not game_active:
        scroll -= scroll_speed
        if abs(scroll) > background.get_width():
            scroll = 0
        start_game = draw_starting_page(scroll)
    if game_active:
        draw_background()
        br = draw_bird(bird_pos)
        tr1, tr2 = draw_tunnels(tunnel_pos1, gap1)
        tr3, tr4 = draw_tunnels(tunnel_pos2, gap2)
        tr5, tr6 = draw_tunnels(tunnel_pos3, gap3)
        tr7, tr8 = draw_tunnels(tunnel_pos4, gap4)
        draw_score()
        ground_rect =pygame.Rect(0,620,800,170)
        if not falling:
            bird_velocity += gravity
            bird_pos += bird_velocity
            tunnel_pos1 -= 4
            tunnel_pos2 -= 4
            tunnel_pos3 -= 4
            tunnel_pos4 -= 4
            if 110 > tunnel_pos1 and not pass1:
                pass1 = True
                score += 1
            if 110 > tunnel_pos2 and not pass2:
                pass2 = True
                score += 1
            if 110 > tunnel_pos3 and not pass3:
                pass3 = True
                score += 1
            if 110 > tunnel_pos4 and not pass4:
                pass4 = True
                score += 1

            if bird_pos <= 0:
                bird_pos = 0
                bird_velocity = 0
            if tunnel_pos1 < -100:
                tunnel_pos1 = tunnel_pos4 + 300
                gap1 = random.randint(200, 400)
                pass1 = False
            if tunnel_pos2 < -100:
                tunnel_pos2 = tunnel_pos1 + 300
                gap2 = random.randint(200, 400)
                pass2 = False
            if tunnel_pos3 < -100:
                tunnel_pos3 = tunnel_pos2 + 300
                gap3 = random.randint(200, 400)
                pass3 = False
            if tunnel_pos4 < -100:
                tunnel_pos4 = tunnel_pos3 + 300
                gap4 = random.randint(200, 400)
                pass4 = False
            if br.colliderect(ground_rect) or br.colliderect(tr1) or br.colliderect(tr2) or br.colliderect(tr3) or br.colliderect(tr4) or br.colliderect(tr5) or br.colliderect(tr6) or br.colliderect(tr7) or br.colliderect(tr8):
                falling = True
        if falling and not restart:
            br = draw_bird(bird_pos)
            if not waiting:
                waiting = True
                crash_time = pygame.time.get_ticks()
            if waiting:
                if current_time - crash_time >= 100:
                    bird_velocity += gravity
                    bird_pos += bird_velocity
            if bird_pos > screen.get_height():
                restart = True
        if restart:
            restart_button = draw_game_over()
    pygame.display.update()
    clock.tick(60)
pygame.quit()