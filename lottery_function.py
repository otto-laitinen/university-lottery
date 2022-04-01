from Classes.lotteryticketClass import Lotteryticket
import random


def lottery(contestants):
    # Give all contestants a ticket with a unique id
    id = 0
    underage_contestants = []
    for contestant in contestants:
        if contestant.get_age() < 18:
            underage_contestants.append(contestant)
        else:
            contestant.set_tickets(Lotteryticket(id))
            id += 1

    # List of contestants that are not old enough to participate
    amount_of_underage = len(underage_contestants)
    print(f"{amount_of_underage} underage contestants removed from the lottery")

    # Define winner
    winner = random.choice(contestants)

    return winner
