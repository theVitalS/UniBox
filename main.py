import pygame
import gradient
import menu


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

screen_rect = pygame.Rect(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH)
gradient = gradient.gradientRect((48, 133, 200), (10, 17, 59), screen_rect)

m1 = menu.MenuItem("assets/mail.png", "MAIL 1", (30, 20))
m2 = menu.MenuItem("assets/mail.png", "MAIL 2", (270, 20))
m3 = menu.MenuItem("assets/mail.png", "MAIL 3", (540, 20))
f1 = menu.MenuItem("assets/file.png", "FILE 1", (30, 220))
f2 = menu.MenuItem("assets/file.png", "FILE 2", (270, 220))
f3 = menu.MenuItem("assets/file.png", "FILE 3", (540, 220))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            if m1.ison():
                print("Menu 1 Clicked")

            if m2.ison():
                print("Menu 2 Clicked")

            if m3.ison():
                print("Menu 3 Clicked")

            if f1.ison():
                print("File 1 Clicked")

            if f2.ison():
                print("File 2 Clicked")

            if f3.ison():
                print("File 3 Clicked")

    screen.blit(gradient, screen_rect)
    m1.bilt(screen)
    m2.bilt(screen)
    m3.bilt(screen)
    f1.bilt(screen)
    f2.bilt(screen)
    f3.bilt(screen)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
