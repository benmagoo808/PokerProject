class GameStats():
    """ Track stats for poker trainer """

    def __init__(self):
        self.phase = 0
        self.stats_reset()
        self.cards = ['card_back', 'card_back', 'card_back', 'card_back',
                      'card_back', 'card_back', 'card_back']

    def stats_reset(self):
        self.phase = 0
        self.cards = ['card_back', 'card_back', 'card_back', 'card_back',
                      'card_back', 'card_back', 'card_back']

    def move_forward(self):
        self.phase += 1