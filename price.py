from Classes.personClass import Person
from Classes.studentClass import Student
from Classes.teacherClass import Teacher


def price(winner):
<<<<<<< HEAD
=======
    print(f"hi {winner.get_first_name()}")
>>>>>>> 09d28531ad242e1c49dee7ddb79059d07ab1b2e2

    if isinstance(winner, Student):
        print(f"{winner.get_first_name()} is a student")

    elif isinstance(winner, Teacher):
        print(f"{winner.get_first_name()} is a teacher")

    else:
        print(f"{winner.get_first_name()} is a regular person")
