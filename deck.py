# deck.py

from random import randrange


class Deck:
    """ Standard Oops! deck. The draw() method allows one to randomly choose
    from this deck. """

    def __init__(self):
        """ Initialize Oops! deck. """
        # create standard 45-card Oops! deck
        self.deck = ([1] * 5 + [2] * 4 + [3] * 4 + [4] * 4 +
                     [5] * 4 + [7] * 4 + [8] * 4 + [10] * 4 + [11] * 4
                     + [12] * 4 + ["Oops!"] * 4)

    def draw(self):
        """ Draw a random card from Oops! deck.
            Output: Oops! card. """
        if len(self.deck) > 0:
            # choose random card within the Oops! deck
            randomNumber = randrange(0, len(self.deck))
            toDraw = self.deck[randomNumber]
            # remove that card from Oops! deck
            self.deck.remove(toDraw)
            return toDraw
        else:
            # replenish deck
            self.deck = ([1] * 5 + [2] * 4 + [3] * 4 + [4] * 4 + [5] * 4
                         + [7] * 4 + [8] * 4 + [10] * 4 + [11] * 4
                         + [12] * 4 + ["Oops!"] * 4)
            # draw from deck
            self.draw()
