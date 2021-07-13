import pygame, sys, os
from card import Card

width, height = 900, 500
pygame.display.set_caption("Dumb")
win = pygame.display.set_mode((width, height))


def draw_window(screen, players):
    screen.fill((255, 255, 255))
    for player in reversed(players):
        player.draw(screen)
    pygame.display.update()


def generate_cards():
    cards = os.listdir("cards")
    deck = [Card(50, 50, 100, 145) for i in range(54)]
    for x in range(54):
        deck[x].image = pygame.image.load(os.path.join("cards", cards[x]))
        deck[x].image.convert()
    return deck


def main():
    run = True
    clock = pygame.time.Clock()
    deck = generate_cards()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for card in deck:  # this is card moving logic
            if card.move():
                deck.insert(0, deck.pop(deck.index(card)))
                break
        draw_window(win, deck)


if __name__ == "__main__":
    main()
