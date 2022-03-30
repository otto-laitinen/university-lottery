from Classes.lotteryticketClass import Lotteryticket
import random


def lottery(contestants):
    # Give all contestants a ticket with a unique id
    id = 0
    for contestant in contestants:
        contestant.set_ticket(Lotteryticket(id))
        id += 1

    # Define winner
    winner = random.choice(contestant)

    return winner
