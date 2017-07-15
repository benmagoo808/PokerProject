import pygame
from settings import Settings
import sys
from button import Button
from images import DeckImage, CardBack, Hand
import game_functions as gf


def run_game():
    # Import the settings from the Settings class
    pt_set = Settings()
    bg_color = pt_set.bg_color
    screen_width = pt_set.screen_width
    screen_height = pt_set.screen_height
    caption = pt_set.caption

    # Initialize the game and draw the game window
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)

    # Initialize the objects within the window
    deal_button = Button(screen, "Deal")
    deck_image = DeckImage(screen)

    # Initialize a separate instance for each card on the table
    # Passing the screen and the card number on table, then card value as str
    card_1 = CardBack(screen, 1, 'Ace-Clubs')
    card_2 = CardBack(screen, 2, 'card_back')
    card_3 = CardBack(screen, 3, 'card_back')
    card_4 = CardBack(screen, 4, 'card_back')
    card_5 = CardBack(screen, 5, 'card_back')
    hand_1 = Hand(screen, 1, 'card_back')
    hand_2 = Hand(screen, 2, 'card_back')


    # Start main game loop
    while True:
        gf.check_events()

        gf.update_screen(pt_set, screen, deal_button, deck_image, card_1,
                      card_2, card_3, card_4, card_5, hand_1, hand_2)



run_game()