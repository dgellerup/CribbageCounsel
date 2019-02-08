

class Deck:

    card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_suits = ['D', 'S', 'C', 'H']

    def __init__(self):

        self.card_list = []

        for suit in Deck.card_suits:
            for value in Deck.card_values:

                card = f"{value}-{suit}"
                self.card_list.append(card)


    def deal_cards(self, player_cards):

        self.dealt_cards = player_cards

        for card in player_cards:
            self.card_list.remove(card)
