import pygame, sys, os
from card import Card


class Deck(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_folder, back_path):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image_folder = image_folder
        self.cards_list = os.listdir(image_folder)
        self.back = pygame.image.load(os.path.join(image_folder, back_path))
        self.image = self.back
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.deck = pygame.sprite.Group()

    def clicked(self):
        return pygame.mouse.get_pressed(3)[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def add_card(self):
        card_name = self.cards_list.pop(0)
        card = Card(self.pos_x, self.pos_y, self.image_folder, card_name, self.back, True)
        card.held = True
        self.deck.add(card)
# test comment