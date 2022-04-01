from Classes.personClass import Person
from Classes.studentClass import Student
from Classes.teacherClass import Teacher


def price(winner, university):

    # If winner is a student --> give extra credit
    if isinstance(winner, Student):
        print(f"Winner is a student with {winner.get_credits()} credits")
        winner.set_credits(winner.get_credits() + 1)
        print(
            f"{winner.get_first_name()} receives 1 extra credit! New credits: {winner.get_credits()} "
        )

    # If winner is a teacher --> give extra day off
    elif isinstance(winner, Teacher):
        print(f"Winner is a teacher with {winner.get_days_off()} days off")
        winner.set_days_off(winner.get_days_off() + 1)
        print(
            f"{winner.get_first_name()} receives 1 extra day off! New amount of days off: {winner.get_days_off()} "
        )

    # If winner is a regular person --> give them a study place
    else:
        winner = Student(
            winner.get_first_name(),
            winner.get_last_name(),
            winner.get_age(),
            None,
            university,
            0,
        )
        print(
            f"{winner.get_first_name()} is not a member of any university. They receive a free study place!"
        )
        print(
            f"{winner.get_first_name()} is now a student at {winner.get_institute().get_name()}"
        )
