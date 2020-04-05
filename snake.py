import pygame
import random
import time


class GameObject:

    def __init__(self, file, spawnX, spawnY):
        self.file = pygame.image.load(file)
        self.spawnX = spawnX
        self.spawnY = spawnY

        self.nextX = spawnX
        self.nextY = spawnY
    def show(self, img, x, y):
        screen.blit(img, (x, y))
    def check_boundries(self):
        if self.nextX > 736 or self.nextX < 0:
            return False
        if self.nextY > 536 or self.nextY < 0:
            return False
    def update_pos(self):
        self.spawnX = self.nextX
        self.spawnY = self.nextY
    def set_next(self, x, y):
        self.nextX = x
        self.nextY = y
    def returnX(self):
        return self.spawnX
    def returnY(self):
        return self.spawnY




# ------- PyGame ------- #
# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Snake, In Python")

# https://www.flaticon.com/authors/freepik
icon = pygame.image.load('hss.png')
pygame.display.set_icon(icon)
# ------- EndPygame ------- #



# ------- Game Loop ------- #

# Obj creation
player = [GameObject('u.png', 370, 480), GameObject('W.png', 370, 480+64), GameObject('u.png', 370, 480+64+64), GameObject('W.png', 370, 480+64+64+64)]
apple = GameObject('apple.png', random.randint(0, 736), random.randint(0, 536))

# extra functions
def NEXT(player, left_right, up_down):
    player[0].set_next(player[0].returnX() + left_right, player[0].returnY() + up_down)
    if len(player) >= 2:
        for i in range(len(player) - 1):
            player[i+1].set_next(player[i].returnX(), player[i].returnY())

def collide():
    return

jump = 10+64

running = True
left, right, up, down = False, False, False, False
difficulty = .7 # seconds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # checks for the left arrow
            if event.key == pygame.K_LEFT:
                if right:
                    continue
                left = True
                right, up, down = False, False, False
            elif event.key == pygame.K_RIGHT:
                if left:
                    continue
                right = True
                left, up, down = False, False, False
            elif event.key == pygame.K_UP:
                if down:
                    continue
                up = True
                left, right, down = False, False, False
            elif event.key == pygame.K_DOWN:
                if up:
                    continue
                down = True
                left, right, up = False, False, False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key up") # Keep this in for now.
    if left:
        NEXT(player, -jump, 0)
    elif right:
        NEXT(player, jump, 0)
    elif up:
        NEXT(player, 0, -jump)
    elif down:
        NEXT(player, 0, jump)
    screen.fill((101, 101, 101))
    apple.show(apple.file, apple.spawnX, apple.spawnY)
    for obj in player:
        obj.update_pos()
        obj.show(obj.file, obj.spawnX, obj.spawnY)
        screen.blit(icon, (obj.spawnX, obj.spawnY)) # Debug tool
        screen.blit(icon, (obj.spawnX+64, obj.spawnY+64)) # Debug tool

    pygame.display.update()
    time.sleep(difficulty)

pygame.quit()

"""
Abstract away the render from the logic

Make a matrix that holds the location of the snake

"""
