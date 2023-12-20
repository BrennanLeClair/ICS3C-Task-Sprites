import pygame

cat_image = pygame.image.load("cat.png")
cat_image_flipped = pygame.transform.flip(cat_image, True, False)

class Cat (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cat_image
        self.rect = cat_image.get_rect(center=(130, 70))
        self.speed = 0.7