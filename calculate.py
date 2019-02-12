from itertools import combinations

import hand
import deck

def multiples(hand):

    #print("\nMULTIPLES\n")

    uniques = set(hand.cards)

    hand.counts_dict = {}

    for card in uniques:
        hand.counts_dict[card] = hand.cards.count(card)

    for key in hand.counts_dict:
        #print(f"Card Value {key}: {hand.counts_dict[key]}")
        if hand.counts_dict[key] == 2:
            hand.score += 2
            #print("Worth: 2")
        elif hand.counts_dict[key] == 3:
            hand.score += 6
            #print("Worth: 6")
        elif hand.counts_dict[key] == 4:
            hand.score += 12
            #print("Worth: 12")
        #else:
            #print("Worth: 0")
        #print(f"Score: {hand.score}\n")


def fifteens(hand):

    #print("\nFIFTEENS\n")
    hand.card_values = [hand.card_dict[card] for card in hand.cards]

    for i in range(2, len(hand.card_values)+1):
        #print(f"Combination Size: {i}")
        for combo in combinations(hand.card_values, i):
            if sum(combo) == 15:
                hand.score += 2

            #print(f"Combo: {combo}  Score: {hand.score}")
        #print()

    return hand.score


def suits(hand):

    #print(hand.suits)

    uniques = set(hand.suits)

    hand.suits_dict = {}

    for card in uniques:
        hand.suits_dict[card] = hand.suits.count(card)

    #print(hand.suits_dict)

    for key in hand.suits_dict:
        if hand.suits_dict[key] > 3:
            hand.score += hand.suits_dict[key]
            #print(f"Worth: {hand.suits_dict[key]}")
            #print(f"Score: {hand.score}")


def runs(hand):

    hand.ordered_cards = [hand.card_order[card] for card in hand.cards]
    hand.ordered_cards.sort()
    #print()
    #print("\nRUNS\n")
    #print(hand.cards)
    #print(hand.card_order)

    run_value = 0

    if hand.ordered_cards[2] == hand.ordered_cards[1]+1 \
        and hand.ordered_cards[1] == hand.ordered_cards[0]+1:

        run_value = 3

        if hand.ordered_cards[3] == hand.ordered_cards[2]+1:
            run_value = 4

    elif hand.ordered_cards[3] == hand.ordered_cards[2]+1 \
        and hand.ordered_cards[2] == hand.ordered_cards[1]+1:

        run_value = 3

    if hand.ordered_cards[0] == hand.ordered_cards[1] \
        and hand.ordered_cards[1]+1 == hand.ordered_cards[2] \
        and hand.ordered_cards[2]+1 == hand.ordered_cards[3]:

        run_value = 6

    if hand.ordered_cards[0]+1 == hand.ordered_cards[1] \
        and hand.ordered_cards[1] == hand.ordered_cards[2] \
        and hand.ordered_cards[2]+1 == hand.ordered_cards[3]:

        run_value = 6

    if hand.ordered_cards[0]+1 == hand.ordered_cards[1] \
        and hand.ordered_cards[1]+1 == hand.ordered_cards[2] \
        and hand.ordered_cards[2] == hand.ordered_cards[3]:

        run_value = 6

    #print(f"Run Value: {run_value}")

    hand.score += run_value

    #print(f"Score: {hand.score}\n")


def score_hand(hand):

    multiples(hand)
    fifteens(hand)
    suits(hand)
    runs(hand)


def can_run(ordered_cards):

    potential_run = False

    for i in range(len(ordered_cards)-1):
        if ordered_cards[i+1] - ordered_cards[i] == 1:
            potential_run = True
        if ordered_cards[i+1] - ordered_cards[i] == 2:
            potential_run = True

    return potential_run


def find_run(ordered_cards):

    needed = []

    for i in range(len(ordered_cards)-1):
        if ordered_cards[i+1] - ordered_cards[i] == 1:
            needed.append(ordered_cards[i]-1)
            needed.append(ordered_cards[i+1]+1)
        if ordered_cards[i+1] - ordered_cards[i] == 2:
            needed.append(ordered_cards[i]+1)

    needed = set(needed)
    temp_ordered = set(ordered_cards)

    needed = needed - temp_ordered
    print(f"Final needed: {needed}")

    translated_needed = []

    for card in needed:
        for key, value in hand.Hand.card_order.items():
            if value == card:
                translated_needed.append(key)
    print(translated_needed)
    return translated_needed


def run_card(combination, the_deck):

    likelihood = 0

    ordered_cards = [hand.Hand.card_order[card.split("-")[0]] for card in combination]
    ordered_cards.sort()
    print(f"ordered_cards: {ordered_cards}")

    if can_run(ordered_cards):
        cards_needed = find_run(ordered_cards)
    else:
        print("return 0")
        return 0

    cards_in_deck = sum([int(the_deck.values[key]) for key in the_deck.values])

    num_possible_cards = 0

    for card in cards_needed:
        print(card, type(card))
        print(the_deck.values[card])
        num_possible_cards += the_deck.values[card]

    print(num_possible_cards)
    print(f"Likelihood: {num_possible_cards}/{cards_in_deck}={num_possible_cards/cards_in_deck}")
    likelihood = num_possible_cards/cards_in_deck

    return f"{round(likelihood*100, 1)}%"


def potential_runs(df, the_deck):

    print(the_deck.values)

    df['For Run'] = df['Combination'].apply(run_card, the_deck=the_deck)

    return df
