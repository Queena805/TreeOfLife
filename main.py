import pygame
import os
import random
from pygame.locals import *
import math

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Tree Of Life")
icon = pygame.image.load('tree.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 50
playerY = 500
playerX_change = 0
playerY_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ghost-costume.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)



#Eggs
green_egg_Img = pygame.image.load('green_egg.png')
green_eggX = random.randint(10,700)
green_eggY = random.randint(60,450)

brown_egg_Img = pygame.image.load('brown_egg.png')
brown_eggX = random.randint(10,700)
brown_eggY = random.randint(60,450)

pink_egg_Img = pygame.image.load('pink_egg.png')
pink_eggX = random.randint(10,700)
pink_eggY = random.randint(60,450)



#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x, y))

def green_egg(x,y):
    screen.blit(green_egg_Img,(x, y))

def brown_egg(x,y):
    screen.blit(brown_egg_Img,(x, y))

def pink_egg(x,y):
    screen.blit(pink_egg_Img,(x, y))

def collect_egg(green_eggX,green_eggY,playerX,playerY):
    distance = math.sqrt((math.pow(green_eggX - playerX, 2)) + (math.pow(green_eggY - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

def isCollision(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY-playerY,2)))
    if distance < 27:
        return True
    else:
        return False




#game loop
running = True
while running:
    # pygame.time.delay(1000)

    # rgb = red, green, blue
    screen.fill((126, 186, 78))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # 5 = 5 + -o.1 -> 5- - 0.1
    # Player Movement
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >=525:
        playerY = 525


    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

    #Collect_egg
    get_egg = collect_egg(green_eggX,green_eggY,playerX,playerY)
    if get_egg:
        score_value += 2
        print(f"Congrats! You get the egg! You score is {score_value}.")
        green_eggX = random.randint(10, 700)
        green_eggY = random.randint(60, 450)

    #Collision
    collision = isCollision(enemyX[i],enemyY[i],playerX,playerY)
    if collision:
        score_value -= 1
        print(f"Collision happen!! Your score is {score_value}")
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)

    enemy(enemyX[i],enemyY[i], i)

    green_egg(green_eggX, green_eggY)
    brown_egg(brown_eggX, brown_eggY)
    pink_egg(pink_eggX, pink_eggY)

    player(playerX, playerY)
    show_score(textX,testY)

    pygame.display.update()