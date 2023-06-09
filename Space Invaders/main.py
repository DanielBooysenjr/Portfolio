# Space Invaders Game
    # # PyGame Tutorial - Youtube

import pygame
import math
import random
# Loading music and sound
from pygame import mixer

# Initialize the PyGame
pygame.init()

# Title and Icon of Game - Doing this before creating the screen makes the refresh faster
title = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Setting game background
background = pygame.image.load("background.png")

# Background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Loading bullet
bullet = pygame.image.load("bullet.png")

# Create the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Player
player_image = pygame.image.load("player1.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):

    enemy_image.append(pygame.image.load("player2.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - Bullet is currently moving
bullet_image = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.8
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 64)

def game_over():
    over_text = over_font.render("GAME OVER!", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))


# Player Function
def player(x, y):
    ''' Pass the x and y coor of the player'''
    # Drawing the player on screen. Requires image, and X & Y value in a tuple
    screen.blit(player_image, (x, y))

# Player Function
def enemy(x, y, i):
    ''' Pass the x and y coor of the player'''
    # Drawing the player on screen. Requires image, and X & Y value in a tuple
    screen.blit(enemy_image[i], (x, y))

# Bullet function
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x+16, y+10))

# Checking collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


# Creating main game loop
running = True
while running:
    # Changing screen fill color
    screen.fill((0, 0, 0))
    # Adding the background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Checking if keystroke is pressed, change player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # Get current X coor of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Setting up screen edge boundries for player
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Setting up screen edge boundries for enemy
    for i in range (num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range (num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5



            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            if score_value == 2:
                enemy(enemyX[i], enemyY[i], i)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)



        enemy(enemyX[i], enemyY[i], i)
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    


    # Calling player function and position
    player(playerX , playerY)
    # Calling Score
    show_score(textX, textY)
    # Updating the screen - Refreshing the screen
    pygame.display.update()