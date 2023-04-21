import pygame
import gradient


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
                                self.textRect.height+self.image_rect.y+self.image_rect.height+20)

    def bilt(self, screen):
        pygame.draw.rect(screen, (20, 42, 79), self.backRect)
        screen.blit(self.image, (self.pos[0]+20, self.pos[1]+20))
        screen.blit(self.text, self.textRect)

    def ison(self):
        return self.backRect.collidepoint(pygame.mouse.get_pos())




WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

screen_rect = pygame.Rect(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH)
gradient = gradient.gradientRect((48, 133, 200), (10, 17, 59), screen_rect)

mail = MenuItem("assets/mail.png", "MAIL", (10, 20))
file = MenuItem("assets/file.png", "FILE", (300, 20))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mail.ison():
                print("Menu Clicked")

            if file.ison():
                print("File Clicked")

    screen.blit(gradient, screen_rect)
    mail.bilt(screen)
    file.bilt(screen)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
