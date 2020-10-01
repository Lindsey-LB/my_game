# The objective of this game is to retrieve the prize (static)
# while avoiding the enemies streaming(moving) across the screen.

import pygame
import random

pygame.init()

# Create the screen
screen_height = 700
screen_width = 1040
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load("background.png")

# Title & icon
pygame.display.set_caption("Nostalgia")
icon = pygame.image.load("castle.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 100
playerY = 340
playerX_change = 0
playerY_change = 0
player_height = playerImg.get_height()
player_width = playerImg.get_width()

def player(x,y):
    screen.blit(playerImg, (x, y))

# Prize
prizeImg = pygame.image.load("prize.png")
prize_width = prizeImg.get_width()
prize_height = prizeImg.get_height()
prizeX = screen_width - 150
prizeY = random.randint(40, screen_height - prize_height)

def prize(x,y):
    screen.blit(prizeImg, (x, y))
    
# Enemies
bulletImg = []
bulletX = []
bulletY = []
bulletX_change = []
num_bullets = 4

for i in range(num_bullets):
    bulletImg.append(pygame.image.load("enemy.png"))
    bullet_height = bulletImg[0].get_height()
    bullet_width = bulletImg[0].get_width()
    bulletX.append(screen_width)
    bulletY.append(random.randint(40, screen_height - bullet_height))
    bulletX_change.append(-3)

def bullet(x,y, i):
    screen.blit(bulletImg[i], (x, y))

#Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if playerY > 40:
                    playerY_change = -3
            if event.key == pygame.K_DOWN:
                if playerY < (screen_height - player_height - 30):

                    playerY_change = 3
            if event.key == pygame.K_LEFT:
                if playerX > 20:
                    playerX_change = -3
            if event.key == pygame.K_RIGHT:
                if playerX < (screen_width - player_width -20):
                    playerX_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Boundary box for player
    playerBox = pygame.Rect(playerImg.get_rect())
    playerBox.top = int(playerY)
    playerBox.left = int(playerX)

    # Bounday box for prize
    prizeBox = pygame.Rect(prizeImg.get_rect())
    prizeBox.top = int(prizeY)
    prizeBox.left = int(prizeX)

    if playerBox.colliderect(prizeBox):
        running = False
        print("You win!")
        pygame.quit()
        exit(0)

    # Boundary box for enemies
    for i in range(num_bullets):
        bulletBox = pygame.Rect(bulletImg[i].get_rect()) # List for bullet box?
        bulletBox.top = int(bulletY[i])
        bulletBox.left = int(bulletX[i])

        if playerBox.colliderect(bulletBox):
            running = False
            print("You lose!")
            pygame.quit()
            exit(0)
   
    playerX += playerX_change
    playerY += playerY_change

# Enemy Movement
    for i in range(num_bullets):
        if bulletX[i] > 0:
            bulletX[i] += bulletX_change[i]
        elif bulletX[i] < 0:
            bulletX[i] = screen_width
            bulletY[i] = random.randint(40, screen_height - bullet_height)
    
    player(playerX, playerY)
    prize(prizeX, prizeY)
        
    for i in range(num_bullets):
        bullet(bulletX[i], bulletY[i], i)

    pygame.display.update()
    
