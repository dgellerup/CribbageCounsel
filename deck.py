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


    def get_stats(self):

        suits_dict = {}
        values_dict = {}

        for card in self.card_list:
            if card.split("-")[0] in values_dict:
                values_dict[card.split("-")[0]] += 1
            else:
                values_dict[card.split("-")[0]] = 1

            if card.split("-")[1] in suits_dict:
                suits_dict[card.split("-")[1]] += 1
            else:
                suits_dict[card.split("-")[1]] = 1

        self.suits = suits_dict
        self.values = values_dict
        

    def reset_deck(self):

        self.card_list.extend(self.dealt_cards)
