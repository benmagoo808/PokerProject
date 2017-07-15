import pygame
from settings import Settings
from button import Button
import cards as pt_cards
import game_functions as gf
import stats as st


def run_game():
    # Import the settings from the Settings class
    pt_set = Settings()
    screen_width = pt_set.screen_width
    screen_height = pt_set.screen_height
    caption = pt_set.caption
    # Create an instance of the stats class
    pt_stats = st.GameStats()

    # Initialize the game and draw the game window
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)

    # Initialize the objects within the window
    deal_button = Button(screen, "Deal")
    deck_image = pt_cards.DeckImage(screen)

    # Initialize a separate instance for each card on the table
    # Passing the screen and the card number on table, then card value as str
    card_1 = pt_cards.CardBack(screen, 1, 'card_back')
    card_2 = pt_cards.CardBack(screen, 2, 'card_back')
    card_3 = pt_cards.CardBack(screen, 3, 'card_back')
    card_4 = pt_cards.CardBack(screen, 4, 'card_back')
    card_5 = pt_cards.CardBack(screen, 5, 'card_back')
    hand_1 = pt_cards.Hand(screen, 1, 'card_back')
    hand_2 = pt_cards.Hand(screen, 2, 'card_back')


    # Start main game loop
    while True:
        gf.check_events(deal_button)

        gf.update_screen(pt_set, screen, deal_button, deck_image, card_1,
                         card_2, card_3, card_4, card_5, hand_1, hand_2)



run_game()