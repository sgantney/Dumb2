import pygame
import sys, os
from player import Player

width, height = 900, 500
pygame.display.set_caption("Dumb")
win = pygame.display.set_mode((width, height))


def draw_window(screen, players):
    screen.fill((255, 255, 255))
    for player in reversed(players):
        # player.draw(screen)
        screen.blit(player.image, (player.x, player.y))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    players = [Player(50, 50, 100, 145, (255, 0, 0)) for i in range(1)]
    players[0].image = pygame.image.load(os.path.join("2_of_clubs.png"))
    players[0].image.convert()
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
