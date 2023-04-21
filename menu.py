import pygame

class MenuItem:
    def __init__(self, image, text, position):
        self.image = pygame.image.load(image)
        self.pos = position
        self.image_rect = self.image.get_rect()
        self.backRect = pygame.Rect(position[0], position[1],
                                    self.image_rect.width+40, self.image_rect.height+55)

        self.font = pygame.font.Font('fonts/KdamThmor.ttf', 25)
        self.text = self.font.render(text, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.backRect.width//2+self.backRect.x,
                                self.backRect.height+self.backRect.y-self.textRect.height//2)

    def bilt(self, screen):
        pygame.draw.rect(screen, (20, 42, 79), self.backRect)
        screen.blit(self.image, (self.pos[0]+20, self.pos[1]+20))
        screen.blit(self.text, self.textRect)

    def ison(self):
        return self.backRect.collidepoint(pygame.mouse.get_pos())


