import pygame
import gradient

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

screen_rect = pygame.Rect(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH)
gradient = gradient.gradientRect((48, 133, 200), (10, 17, 59), screen_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(gradient, screen_rect)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
