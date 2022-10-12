from cgitb import grey
from random import random
import pygame
import os
WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zerlog")
WHITE = (255,255,255)

FPS = 144

class Player:
    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            self.dy -= 0.3
        if keys_pressed[pygame.K_s]:
            self.dy += 0.3
        if keys_pressed[pygame.K_d]:
            self.dx += 0.3
        if keys_pressed[pygame.K_a]:
            self.dx -= 0.3
        self.dx *= 0.96
        self.dy += 0.2
        if self.x < 0:
            self.x = 0
            self.dx *= -0.9
        if self.y < 0:
            self.y = 0
            self.dy *= -0.9
        if self.x > 900 - 32:
            self.x = 900 - 32
            self.dx *= -0.9
        if self.y > 500 - 32:
            self.y = 500 - 32
            self.dy *= -0.6

        self.x += self.dx
        self.y += self.dy


FACE_IMAGE = pygame.image.load(
    os.path.join('assets','face.png'))
shape = pygame.surface.Surface(
    (100,100))
def draw_window(player):
    WIN.fill(WHITE)
    WIN.blit(FACE_IMAGE,(player.x,player.y))
    pygame.draw.line(WIN, (100,100,100), (player.x + 16, player.y + 16), (player.x + 16 + player.dx*10, player.y+ 16 + player.dy*10))
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        pygame.draw.line(WIN, (255,0,0), (player.x + 16, player.y + 32), (player.x + 16, player.y + 64))
    pygame.display.update()

def main():
    player = Player()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(player)
        player.update()
    pygame.quit()

if __name__ == "__main__":
    main()