from itertools import combinations

def multiples(hand):

    print("\nMULTIPLES\n")

    uniques = set(hand.cards)

    hand.counts_dict = {}

    for card in uniques:
        hand.counts_dict[card] = hand.cards.count(card)

    for key in hand.counts_dict:
        print(f"Card Value {key}: {hand.counts_dict[key]}")
        if hand.counts_dict[key] == 2:
            hand.score += 2
            print("Worth: 2")
        elif hand.counts_dict[key] == 3:
            hand.score += 6
            print("Worth: 6")
        elif hand.counts_dict[key] == 4:
            hand.score += 12
            print("Worth: 12")
        else:
            print("Worth: 0")
        print(f"Score: {hand.score}\n")


def fifteens(hand):

    print("\nFIFTEENS\n")
    hand.card_values = [hand.card_dict[card] for card in hand.cards]

    if sum(hand.card_values) == 15:
        hand.score += 2

    for i in range(2, len(hand.card_values)+1):
        print(f"Combination Size: {i}")
        for combo in combinations(hand.card_values, i):
            if sum(combo) == 15:
                hand.score += 2

            print(f"Combo: {combo}  Score: {hand.score}")
        print()

    return hand.score


def suits(hand):

    print(hand.suits)

    uniques = set(hand.suits)

    hand.suits_dict = {}

    for card in uniques:
        hand.suits_dict[card] = hand.suits.count(card)

    print(hand.suits_dict)

    for key in hand.suits_dict:
        if hand.suits_dict[key] > 3:
            hand.score += hand.suits_dict[key]
            print(f"Worth: {hand.suits_dict[key]}")
            print(f"Score: {hand.score}")


def runs(hand):

    hand.card_order = [hand.card_order[card] for card in hand.cards]
    hand.card_order.sort()
    print()
    print("\nRUNS\n")
    print(hand.cards)
    print(hand.card_order)

    run_value = 0

    if hand.card_order[2] == hand.card_order[1]+1 \
        and hand.card_order[1] == hand.card_order[0]+1:

        run_value = 3

        if hand.card_order[3] == hand.card_order[2]+1:
            run_value = 4

    elif hand.card_order[3] == hand.card_order[2]+1 \
        and hand.card_order[2] == hand.card_order[1]+1:

        run_value = 3

    if hand.card_order[0] == hand.card_order[1] \
        and hand.card_order[1]+1 == hand.card_order[2] \
        and hand.card_order[2]+1 == hand.card_order[3]:

        run_value = 6

    if hand.card_order[0]+1 == hand.card_order[1] \
        and hand.card_order[1] == hand.card_order[2] \
        and hand.card_order[2]+1 == hand.card_order[3]:

        run_value = 6

    if hand.card_order[0]+1 == hand.card_order[1] \
        and hand.card_order[1]+1 == hand.card_order[2] \
        and hand.card_order[2] == hand.card_order[3]:

        run_value = 6

    print(f"Run Value: {run_value}")

    hand.score += run_value

    print(f"Score: {hand.score}\n")



def score_hand(hand):

    multiples(hand)
    fifteens(hand)
    suits(hand)
    runs(hand)
