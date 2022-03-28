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


def main():
    university = University("TUAS")
    print(university.name)

    students = [Student("James", "Jameson", 24, university, "student")]
    teachers = [Teacher("Jon", "Jones", 49, university, "teacher")]
    other_people = [Person("Emma", "Li", 20)]
    all_contestants = students + teachers + other_people

    for i in all_contestants:
        print(i.get_first_name())

    lottery_tickets = [Lotteryticket]
    print(lottery_tickets[0])

    # function here to define the winner


main()
