from Classes.personClass import Person
from Classes.studentClass import Student
from Classes.teacherClass import Teacher


def price(winner):
    if isinstance(winner, Student):
        print(f"Winner is a student with {winner.get_credits()} credits")
        winner.set_credits(winner.get_credits() + 1)
        print(
            f"{winner.get_first_name()} receives 1 extra credit! New credits: {winner.get_credits()} "
        )

    elif isinstance(winner, Teacher):
        print(f"Winner is a teacher with {winner.get_days_off()} days off")
        winner.set_days_off(winner.get_days_off() + 1)
        print(
            f"{winner.get_first_name()} receives 1 extra day off! New amount of days off: {winner.get_days_off()} "
        )

    else:
        print(f"{winner.get_first_name()} is a regular person")
