import pygame
from pygame.locals import *
# Intialize the pygame
pygame.init()

# Create the screen 
screen = pygame.display.set_mode((300, 180))


#Title and Icon
pygame.display.set_caption("Fighting Game")

# Add's logo to the window 
# icon = pygame.image.load('')
# pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/charcterfiller.png')
playerX = 150
playerY = 110
def player(x,y):
    screen.blit(playerImg,(x,y))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('images/image.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('image.png', [0,0])

#  Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(BackGround.image, BackGround.rect)
    player(playerX,playerY)
    pygame.display.flip()
