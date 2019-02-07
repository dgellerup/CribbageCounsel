import hand
import calculate

def check_input(deal):

    acceptable_values = list(range(2, 11))
    acceptable_values.extend(["A", "J", "Q", "K"])
    acceptable_values = [str(val) for val in acceptable_values]
    acceptable_suits = ["D", "C", "S", "H"]

    clean_deal = deal.replace(", ", ",").replace(" ", ",").replace(",,", ",")
    print(f'Your entries: {clean_deal.split(",")}')
    print(clean_deal)
    clean_deal = [item for item in clean_deal.split(",") if item != ""]
    print(clean_deal)
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

    if check_input(deal) != True:
        print("Exiting")
        sys.exit()

    player_hand = hand.Hand(deal)

    calculate.score_hand(player_hand)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
