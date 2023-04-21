import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

img = pygame.image.load("hello.jpg")
size = img.get_size()

img = pygame.transform.scale(img, (500, 500))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(img, (0, 0))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
