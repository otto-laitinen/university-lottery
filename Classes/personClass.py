# File name: personClass.py
# Author: (use your name, of course)
# Description: Defines the attributes of a  Person.


class Person:
    def __init__(
        self,
        first_name,
        last_name,
        age,
        tickets,
    ):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_age(age)
        self.set_tickets(tickets)

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_tickets(self, tickets):
        self.tickets = tickets
    
    def get_tickets(self):
        return self.tickets 


