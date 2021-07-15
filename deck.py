import os
import pygame
import random

from datetime import datetime
from card import Card


class Deck:
    def __int__(self, card_x, card_y, card_width, card_height, cards_file, jokers):
        self.card_x = card_x
        self.card_y = card_y
        self.card_width = card_width
        self.card_height = card_height
        self.cards_file = cards_file
        self.cards_list = os.listdir(cards_file)
        self.jokers = jokers
        self.cards_left = 54 if jokers else 52

    def generate_card(self):
        random.seed(datetime.now())  # creates random seed
        rand = random.randint(0, 10000) % self.cards_left  # grabs random card index
        card = Card(self.card_x, self.card_y, self.card_width, self.card_height, False, self.cards_list[rand])
        card.image = pygame.image.load(os.path.join(self.cards_file, card.card_name))
        card.image.convert()
        self.cards_list.pop(rand)
        return card



    #def generate_deck
