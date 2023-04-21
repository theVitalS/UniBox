import pygame
import gradient


class MenuItem:
    def __init__(self, image, text, position):
        self.image = pygame.image.load(image)
        self.pos = position
        image_rect = self.image.get_rect()
        self.backRect = pygame.Rect(position[0], position[1], image_rect.width+40, image_rect.height+40)

    def bilt(self, screen):
        pygame.draw.rect(screen, (20, 42, 79), self.backRect)
        screen.blit(self.image, (self.pos[0]+20, self.pos[1]+20))


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

screen_rect = pygame.Rect(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH)
gradient = gradient.gradientRect((48, 133, 200), (10, 17, 59), screen_rect)

item = MenuItem("assets/mail.png", "Mail", (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(gradient, screen_rect)
    item.bilt(screen)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
