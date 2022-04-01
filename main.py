# File name: main.py
# Author: (use your name, of course)
# Description: Main function for the university lottery.

import random
from os import path
import sys
from playsound import playsound

sys.path.append(path.abspath("./Classes"))

from Classes.personClass import Person
from Classes.studentClass import Student
from Classes.teacherClass import Teacher
from Classes.universityClass import University
from Classes.lotteryticketClass import Lotteryticket

from lottery_function import lottery
from price import price

# opens frist names text file, which is located in the same directory
with open("first_names.txt", "r") as a:
    # reads all of the lines and splits them at the brake, stores in list
    first_names = [line.strip() for line in a]

with open("last_names.txt", "r") as b:
    last_names = [line.strip() for line in b]


def main():
    while True:
        print("                 #### Welcome to TUAS lottery of 2022! ####")
        print(
            "#### The contestants are students,teachers and people from outside the university. ####\n"
        )
        university = University("TUAS")

        students = []
        teachers = []
        other_people = []

        for i in range(100):

            the_random = Student(
                random.choice(first_names),
                random.choice(last_names),
                random.randint(15, 100),
                None,
                university,
                random.randint(0, 250),
            )
            students.append(the_random)

            the_random2 = Teacher(
                random.choice(first_names),
                random.choice(last_names),
                random.randint(15, 100),
                None,
                university,
                random.randint(0, 7),
            )
            teachers.append(the_random2)

            the_random3 = Person(
                random.choice(first_names),
                random.choice(last_names),
                random.randint(15, 100),
                None,
            )
            other_people.append(the_random3)

        all_contestants = students + teachers + other_people

        # Draw the winner
        winner = lottery(all_contestants)

        playsound('/Lottery-horns.wav')

        print(f"Winner is: {winner.get_first_name()} {winner.get_last_name()}")

        # Give the winner a price
        price(winner, university)

        # Play again
        while True:
            play_again = input("Play again? (Y for Yes, N for No): ")
            if play_again.lower() == "y":  # Accepts either Y or y
                play_again = True
                break
            elif play_again.lower() == "n":
                play_again = False
                break
            else:
                print("Enter either Y or N")

        if not play_again:
            break


main()
