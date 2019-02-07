from itertools import combinations

class Hand:

    card_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    card_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}


    def __init__(self, card_string):

        card_string = card_string.replace(", ", ",").replace(" ", ",")

        self.cards = [card.split("-")[0] for card in card_string.split(",") if card.split("-")[0] in Hand.card_dict.keys()]
        self.suits = [card.split("-")[-1] for card in card_string.split(",") if card.split("-")[-1] in ["D", "C", "S", "H"]]
        self.score = 0
