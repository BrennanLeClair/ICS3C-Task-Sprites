import pygame

dog_image = pygame.image.load("dog.png")
dog_image_flipped = pygame.transform.flip(dog_image, True, False)

class Dog (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = dog_image
        self.rect = dog_image.get_rect(center=(200, 200))
        self.speed = 1
        
    def update (self):
        self.rect.x += self.speed