import pygame, sys
from pygame import *

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((50, 30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, pygame.Color('steelblue2'),
                        [(0, 0), (50, 15), (0, 30)])
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.changex = 0 # value to move along x
        self.changey = 0 # value to move along y

    def move_left(self, move_x):
        '''move player left'''
        self.changex -= move_x

    def move_right(self, move_x):
        '''move player right'''
        self.changex += move_x

    def move_up(self, move_y):
        '''move player up'''
        self.changey -= move_y

    def move_down(self, move_y):
        '''move player down'''
        self.changey += move_y

    def update(self):
        '''update player movement'''
        self.rect.x += self.changex
        self.rect.y += self.changey
        self.rotate()
        '''boundary checking'''
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x > WINDOWWIDTH - self.rect.width:
            self.rect.x = WINDOWWIDTH - self.rect.width
        if self.rect.y > WINDOWHEIGHT - self.rect.height:
            self.rect.y = WINDOWHEIGHT - self.rect.height
    def rotate(self):
        direction = tuple(map(
                lambda i, j: i - j, pygame.mouse.get_pos(),
                (self.rect.x, self.rect.y)))
        radius, angle = pygame.math.Vector2(direction).as_polar()
        self.image = pygame.transform.rotate(self.orig_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

WINDOWWIDTH = 500
WINDOWHEIGHT = 400
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('The Lone Character')
active_sprites_list = pygame.sprite.Group()
player = Player(30, 30)
player.rect.x = WINDOWWIDTH / 2 - player.rect.centerx
player.rect.y = 330
active_sprites_list.add(player)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_j:
                player.move_left(5)
            if event.key == pygame.K_d or event.key == pygame.K_l:
                player.move_right(5)
            if event.key == pygame.K_w or event.key == pygame.K_i:
                player.move_up(5)
            if event.key == pygame.K_s or event.key == pygame.K_k:
                player.move_down(5)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_j:
                player.move_left(-5)
            if event.key == pygame.K_d or event.key == pygame.K_l:
                player.move_right(-5)
            if event.key == pygame.K_w or event.key == pygame.K_i:
                player.move_up(-5)
            if event.key == pygame.K_s or event.key == pygame.K_k:
                player.move_down(-5)


    active_sprites_list.update()
    DISPLAYSURF.fill(BLACK)
    active_sprites_list.draw(DISPLAYSURF)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
