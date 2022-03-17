import pygame, sys, random

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height), vsync=True)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font1 = pygame.font.Font("font.ttf", 72)
font2 = pygame.font.Font("font.ttf", 36)
color = (37, 248, 250)
score = 0



def logic():
    full = False
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
        if ball.x >= width - ball.width:
            ball_velocity_x = -ball_velocity_x
        if ball.y <= 0:  # Top
            ball_velocity_y = -ball_velocity_y  # Bounce
        if ball.y >= height - ball.height:  # Bottom
            ball_velocity_y = -ball_velocity_y  # Bounce
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
        if ball.colliderect(player):
            ball_velocity_x = -ball_velocity_x
            score += 1
        if ball.x <= 0:
            return "Lost"
        pygame.display.flip()
        clock.tick(60)


def start():
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
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, player)
        pygame.draw.rect(screen, color, computer)
        pygame.draw.ellipse(screen, color, ball)
        text = font1.render("Pong", True, color)
        fs = font2.render("Press f to toggle full screen", True, color)
        screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height()))
        text = font2.render("Press Enter to start", True, (255, 255, 255))
        screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 + text.get_height() / 2))
        screen.blit(fs, (width / 2 - fs.get_width() / 2, height / 2 + text.get_height() + fs.get_height()))
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
        text2 = font2.render("Press Enter to Continue,Esc to exit", True, color)
        screen.blit(text2, (width / 2 - text2.get_width() / 2, height / 2 + text2.get_height() / 2))
        if is_high:
            screen.blit(high, (width / 2 - high.get_width() / 2, height / 2 + high.get_height() + text.get_height()/2))
        pygame.display.flip()
        clock.tick(60)


playing = True

a = start()
if a == 'Play':
    while playing:
        playin = logic()
        if playin == "Lost":
            lost = game_over()
            if lost == "Play":
                playing = True
