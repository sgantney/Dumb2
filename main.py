import pygame
import sys
from player import Player

width, height = 900, 500
pygame.display.set_caption("Dumb")
win = pygame.display.set_mode((width, height))


def draw_window(screen, players):
    screen.fill((255, 255, 255))
    for player in players:
        player.draw(screen)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    player1 = Player(50, 50, 100, 100, (255, 0, 0))
    player2 = Player(100, 100, 100, 100, (255, 0, 0))
    players = [player1, player2]
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for player in players:
            if player.move():
                players.insert(0, players.pop(players.index(player)))
                break
        draw_window(win, players)


if __name__ == "__main__":
    main()
