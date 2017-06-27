import pygame
from settings import Settings
from button import Button


def run_game():
    # Initialize the game and draw the game window
    pygame.init()
    pt_settings = Settings()
    screen = pygame.display.set_mode((pt_settings.screen_width,
                                     pt_settings.screen_height))
    pygame.display.set_caption("Poker Trainer")

    running = True

    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        pygame.display.update()

    pygame.quit()

run_game()