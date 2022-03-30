# File name: main.py
# Author: (use your name, of course)
# Description: Main function for the university lottery.

from os import path
import sys

sys.path.append(path.abspath("./Classes"))

from Classes.personClass import Person
from Classes.studentClass import Student
from Classes.teacherClass import Teacher
from Classes.universityClass import University
from Classes.lotteryticketClass import Lotteryticket

from lottery_function import lottery
from price import price


def main():
    # Example:
    # with open("first_names.txt", "r") as a:
    #     first_names = a.readlines()

    university = University("TUAS")

    students = [Student("James", "Jameson", 17, None, university, "student")]
    teachers = [Teacher("Jon", "Jones", 49, None, university, "teacher")]
    other_people = [Person("Emma", "Li", 16, None)]
    all_contestants = students + teachers + other_people

    winner = lottery(all_contestants)

    print(f"Winner is: {winner.get_first_name()} {winner.get_last_name()}")

    # give price
    price(winner)


main()
