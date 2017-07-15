import sys
import pygame

def check_events():
    """ Check for events in the game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(pt_set, screen, deal_button, deck_image, card_1, card_2,
                  card_3, card_4, card_5, hand_1, hand_2):
    """ For every iteration of main loop draw the screen """
    # Draw screen at every iteration of main loop
    screen.fill(pt_set.bg_color)
    # Draw Button
    deal_button.draw_button()
    # Draw Deck image (static back of deck)
    deck_image.blitme()
    # Draw the community cards
    card_1.blitme()
    card_2.blitme()
    card_3.blitme()
    card_4.blitme()
    card_5.blitme()
    # Draw the players hand
    hand_1.blitme()
    hand_2.blitme()

    # Refresh the display
    pygame.display.flip()
