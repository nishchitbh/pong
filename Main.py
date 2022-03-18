import pygame, sys, random, os, time

pygame.init()

width = 1280
height = 720

os.environ["SDL_VIDEODRIVER"] = "dummy"

screen = pygame.display.set_mode((width, height), vsync=True)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font1 = pygame.font.Font("font.ttf", 72)
font2 = pygame.font.Font("font.ttf", 36)
color = (37, 248, 250)
score = 0
button_inactive = (255, 255, 255)
button_active = color
settings_color = button_inactive
play_color = button_inactive
exit_color = button_inactive


def settings():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_RETURN:
                    return "Play"
        screen.fill((0, 0, 0))
        text = font1.render("Settings", True, color)
        screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height()))
        text = font2.render("Press Enter to return", True, (255, 255, 255))
        screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 + text.get_height() / 2))
        pygame.display.flip()
        clock.tick(60)


def logic():
    full = False
    bat_hit = pygame.mixer.Sound('bat_hit.mp3')
    wall_hit = pygame.mixer.Sound('wall_hit.mp3')
    global score
    player_height = 150
    player_width = 10
    computer_height = 150
    computer_width = 10
    player_velocity = 0
    score = 0
    computer = pygame.Rect(width - computer_width, height / 2 - computer_height / 2, computer_width, computer_height)
    ball_velocity_x = 7.5 * random.choice([-1, 1])
    ball_velocity_y = 7.5 * random.choice([-1, 1])
    player = pygame.Rect(0, height / 2 - player_height / 2, player_width, player_height)
    ball = pygame.Rect(width / 2 - 10, height / 2 - 10, 20, 20)
    net = pygame.Rect(width / 2 - 5 / 2, 100, 5, height)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_velocity -= 6
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_velocity += 6
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_velocity = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_velocity = 0
        screen.fill((0, 0, 0))
        score_display = font1.render(str(score), True, color)
        screen.blit(score_display, (width / 2 - score_display.get_width() / 2, 5))
        pygame.draw.rect(screen, color, player)
        pygame.draw.rect(screen, color, computer)
        pygame.draw.ellipse(screen, color, ball)
        pygame.draw.rect(screen, color, net)

        # Game Logic
        ball.x += ball_velocity_x
        ball.y += ball_velocity_y
        player.y += player_velocity
        if ball.x <= 0:
            ball_velocity_x = -ball_velocity_x
            pygame.mixer.Sound.play(wall_hit)
        if ball.x >= width - ball.width:
            ball_velocity_x = -ball_velocity_x
            pygame.mixer.Sound.play(wall_hit)
        if ball.y <= 0:  # Top
            ball_velocity_y = -ball_velocity_y  # Bounce
            pygame.mixer.Sound.play(wall_hit)
        if ball.y >= height - ball.height:  # Bottom
            ball_velocity_y = -ball_velocity_y  # Bounce
            pygame.mixer.Sound.play(wall_hit)
        computer.y += ball_velocity_y
        if computer.y <= 0:
            computer.y = 0
        if computer.y >= height - player.height:
            computer.y = height - player.height
        if player.y <= 0:
            player.y = 0
        if player.y >= height - player.height:
            player.y = height - player.height
        if ball.colliderect(computer):
            ball_velocity_x = -ball_velocity_x
            pygame.mixer.Sound.play(bat_hit)
        if ball.colliderect(player):
            ball_velocity_x = -ball_velocity_x
            pygame.mixer.Sound.play(bat_hit)
            score += 1
        if ball.x <= 0:
            return "Lost"
        pygame.display.flip()
        clock.tick(60)


def start():
    global settings_color, play_color, exit_color
    player_height = 150
    player_width = 10
    computer_height = 150
    computer_width = 10
    player_velocity = 0
    computer = pygame.Rect(width - computer_width, height / 2 - computer_height / 2, computer_width, computer_height)
    player = pygame.Rect(0, height / 2 - player_height / 2, player_width, player_height)
    ball = pygame.Rect(width / 2 - 10, height / 2 - 10, 20, 20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_RETURN:
                    return "Play"
        m_x, m_y = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, player)
        pygame.draw.rect(screen, color, computer)
        pygame.draw.ellipse(screen, color, ball)
        text = font1.render("Pong", True, color)
        fs = font2.render("Press f to toggle full screen", True, color)
        screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height()))
        settings = font2.render("Settings", True, settings_color)
        play = font2.render('Play', True, play_color)
        exit = font2.render('Exit', True, exit_color)
        screen.blit(settings, (200, height / 2 + settings.get_height() / 2))
        screen.blit(fs, (width / 2 - fs.get_width() / 2, height / 2 + text.get_height() + fs.get_height()))
        screen.blit(play, (width / 2 - play.get_width() / 2, height / 2 + play.get_height() / 2))
        screen.blit(exit, (width - 200 - exit.get_width(), height / 2 + exit.get_height() / 2))
        if m_x >= 200 and m_x <= 200 + settings.get_width() and m_y >= height / 2 + settings.get_height() / 2 and m_y <= height / 2 + 1.25 * settings.get_height():
            settings_color = button_active
        else:
            settings_color = button_inactive
        if m_x >= width / 2 - play.get_width() / 2 and m_x <= width / 2 + play.get_width() / 2 and m_y >= height / 2 + settings.get_height() / 2 and m_y <= height / 2 + 1.25 * settings.get_height():
            play_color = button_active
        else:
            play_color = button_inactive
        if m_x >= width - 200 - exit.get_width() and m_x <= width - 200 and m_y >= height / 2 + settings.get_height() / 2 and m_y <= height / 2 + 1.25 * settings.get_height():
            exit_color = button_active
        else:
            exit_color = button_inactive
        pygame.display.flip()
        clock.tick(60)


def game_over():
    running = True
    is_high = False
    record = open('highscore.dat', 'r')
    highscore = int(record.readline())
    if score > highscore:
        highscore = score
        record = open('highscore.dat', 'w')
        record.write(str(highscore))
        is_high = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    return "Play"
        screen.fill((0, 0, 0))
        high = font2.render("New Highscore: " + str(highscore), True, color)
        text = font1.render("Game Over", True, color)
        screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height()))
        text2 = font2.render("Press Enter to Continue,Esc to exit", True, (255, 255, 255))
        screen.blit(text2, (width / 2 - text2.get_width() / 2, height / 2 + text2.get_height() / 2))
        if is_high:
            screen.blit(high,
                        (width / 2 - high.get_width() / 2, height / 2 + high.get_height() + text.get_height() / 2))
        pygame.display.flip()
        clock.tick(60)


def timer():
    player_height = 150
    player_width = 10
    computer_height = 150
    computer_width = 10
    player_velocity = 0
    computer = pygame.Rect(width - computer_width, height / 2 - computer_height / 2, computer_width, computer_height)
    player = pygame.Rect(0, height / 2 - player_height / 2, player_width, player_height)
    ball = pygame.Rect(width / 2 - 10, height / 2 - 10, 20, 20)
    net = pygame.Rect(width / 2 - 5 / 2, 100, 5, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
        score_display = font1.render(str(3), True, color)
        for i in range(3, 0, -1):
            text = font1.render(str(i), True, color)
            screen.fill((0, 0, 0))
            screen.blit(text, (width / 2 - text.get_width() / 2, 5))
            pygame.draw.rect(screen, color, player)
            pygame.draw.rect(screen, color, computer)
            pygame.draw.ellipse(screen, color, ball)
            pygame.draw.rect(screen, color, net)
            pygame.display.flip()
            time.sleep(1)
            clock.tick(60)
        return True


playing = True

a = start()
while playing:
    if a == 'Play':
        wait = timer()
        if wait:
            playin = logic()
        if playin == "Lost":
            lost = game_over()
            if lost == "Play":
                playing = True
