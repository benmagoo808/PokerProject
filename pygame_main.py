import pygame
from settings import Settings
import sys
from button import Button



def run_game():
    # Initialize the game and draw the game window
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Poker Trainer")
    bg_color = (230, 230, 230)
    deal_button = Button(screen, "Deal")

    # Start main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw screen at every iteration of main loop
        screen.fill(bg_color)
        # Draw Button
        deal_button.draw_button()
        pygame.display.flip()



run_game()