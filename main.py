# File name: main.py
# Author: (use your name, of course)
# Description: Main function for the university lottery.

from os import path
import sys

sys.path.append(path.abspath("./Classes"))

from Classes.personClass import Person
from Classes.universityClass import University


def main():
    university = University("TUAS")  # test
    print(university.name)

    students = []
    teachers = []
    other_people = []
    all_contestants = students + teachers + other_people
    lottery_tickets = []

    # function here to define the winner


main()
