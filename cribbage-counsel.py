from itertools import combinations

import pandas as pd

import hand
import calculate
import deck

def check_input(deal):

    acceptable_values = list(range(2, 11))
    acceptable_values.extend(["A", "J", "Q", "K"])
    acceptable_values = [str(val) for val in acceptable_values]
    acceptable_suits = ["D", "C", "S", "H"]

    clean_deal = deal.replace(", ", ",").replace(" ", ",").replace(",,", ",")
    print(f'\n\nYour entries: {clean_deal.split(",")}')
    clean_deal = [item for item in clean_deal.split(",") if item != ""]
    is_valid = True

    for item in clean_deal:
        if "-" not in item:
            print(f"Invalid Format: {item}")
            is_valid = False
        else:
            if item.split("-")[0] not in acceptable_values:
                print(f"Invalid Format: {item} (Unknown card value)")
                is_valid = False
            elif item.split("-")[-1] not in acceptable_suits:
                print(f"Invalid Format: {item} (Unknown suit)")
                is_valid = False

    return is_valid


def main(arglist):

    deal = ",".join(arglist)
    deal = deal.upper()

    if check_input(deal) != True:
        print("Exiting")
        sys.exit()

    the_deck = deck.Deck()

    deal_list = [card for card in deal.split(",")]

    the_deck.deal_cards(deal_list)

    score_dict = {}

    for combo in combinations(deal.split(","), 4):
        player_hand = hand.Hand(combo)

        calculate.score_hand(player_hand)

        score_dict[combo] = player_hand.score

    score_df = pd.DataFrame.from_dict(score_dict, orient='index')
    score_df.reset_index(inplace=True)
    score_df.columns = ["Combination", "Score"]

    score_df.sort_values("Score", ascending=False, inplace=True)

    print(score_df)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
