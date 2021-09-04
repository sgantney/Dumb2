import pygame, os


class Card(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_folder, image_path, back_path, flip):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.front = pygame.image.load(os.path.join(image_folder, image_path))
        self.back = pygame.image.load(os.path.join(image_folder, back_path))
        self.image = self.front
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.flip = flip
        self.held = False

    def update(self):
        self.move()
        self.rect.move(self.pos_x, self.pos_y)

    def clicked(self):
        return pygame.mouse.get_pressed(3)[0] and self.rect.collidepoint(pygame.mouse.get_pos())

    def move(self):
        speed = .1
        if self.clicked() or self.held:
            (x, y) = pygame.mouse.get_pos()
            self.pos_x -= speed * (self.pos_x - x)
            self.pos_y -= speed * (self.pos_y - y)
            self.rect.center = (self.pos_x, self.pos_y)
            self.held = True
        if not pygame.mouse.get_pressed(3)[0]:
            self.held = False
