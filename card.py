import pygame, os


class Card:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flip = False
        self.rect = (x, y, width, height)
        self.vel = .1
        self.click = False
        self.image = ""

    def draw(self, win):
        if self.flip:
            win.blit(self.image, (self.x, self.y))
        else:
            back = pygame.image.load(os.path.join("cards", "zback.png"))
            back.convert()
            win.blit(back, (self.x, self.y))

    def clicked(self, mouse_x, mouse_y, left):
        if left:
            if self.x + self.width > mouse_x > self.x and self.y + self.height > mouse_y > self.y:
                self.click = True
                self.flip = True
        else:
            self.click = False

    def move(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        center_x = mouse_x - self.width/2
        center_y = mouse_y - self.height/2
        left, middle, right = pygame.mouse.get_pressed(num_buttons=3)
        self.clicked(mouse_x, mouse_y, left)
        if left and self.click:
            x_dist = abs(center_x - self.x)
            y_dist = abs(center_y - self.y)
            if center_x < self.x:
                self.x -= self.vel * x_dist
            if center_x > self.x:
                self.x += self.vel * x_dist
            if center_y < self.y:
                self.y -= self.vel * y_dist
            if center_y > self.y:
                self.y += self.vel * y_dist
        self.update()
        if self.click:
            return True
        else:
            return False

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
