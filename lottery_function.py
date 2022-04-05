# File name: lottery_function.py
# Author: Otto Laitinen
# Description: Function to draw the winner

from Classes.lotteryticketClass import Lotteryticket
import random


def lottery(contestants):
    # Underage contestants are removed and moved to this list
    underage_contestants = []

    # Ticket id / number
    id = 0

    for contestant in contestants:
        if contestant.get_age() < 18:
            underage_contestants.append(contestant)
            contestant.remove(contestant)
        else:
            contestant.set_tickets(Lotteryticket(id))
            id += 1

    # List of contestants that are not old enough to participate
    amount_of_underage = len(underage_contestants)
    print(f"{amount_of_underage} underage contestants removed from the lottery")

    # Define winner
    winner = random.choice(contestants)

    return winner
