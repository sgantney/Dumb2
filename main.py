import os, pygame, sys
from card import Card

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
width, height = 900, 500
pygame.display.set_caption("Dumb")
screen = pygame.display.set_mode((width, height))

card = Card(200, 200, "cards", "red_joker.png", "zback.png", True)
deck = pygame.sprite.Group()
deck.add(card)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.fill((255, 255, 255))
    deck.draw(screen)
    deck.update()
    clock.tick(60)
