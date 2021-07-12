import pygame
import sys
from player import Player

width, height = 900, 500
pygame.display.set_caption("Dumb")
win = pygame.display.set_mode((width, height))


def draw_window(screen, player):
    screen.fill((255, 255, 255))
    player.draw(screen)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    player = Player(50, 50, 100, 100, (255, 0, 0))
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        player.move()
        draw_window(win, player)


if __name__ == "__main__":
    main()
