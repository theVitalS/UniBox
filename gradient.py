import pygame


# Reference: https://stackoverflow.com/a/62336993
def gradientRect(left_colour, right_colour, target_rect):
    colour_rect = pygame.Surface(( 2, 2 ))
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )
    colour_rect = pygame.transform.rotate(colour_rect, 90);
    return colour_rect


if __name__ == "__main__":
    # Window size
    WINDOW_WIDTH    = 500
    WINDOW_HEIGHT   = 400

    ### initialisation
    pygame.init()
    window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
    pygame.display.set_caption("Gradient Rect")

    screen_rect = pygame.Rect( 0,0, WINDOW_WIDTH, WINDOW_HEIGHT)
    gradient = gradientRect((48, 133, 200), (10, 17, 59), screen_rect)

    ### Main Loop
    clock = pygame.time.Clock()
    finished = False
    while not finished:

        # Handle user-input
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                done = True

        # Update the window

        window.blit(gradient, screen_rect)
        
        pygame.display.flip()

        # Clamp FPS
        clock.tick_busy_loop(60)

    pygame.quit()
