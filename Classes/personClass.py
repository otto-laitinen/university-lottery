# File name: personClass.py
# Author: Salli Saarinen, Otto Laitinen & Thomás Rizzi Omura
# Description: Defines the attributes of a  Person.
class Person:
    #initializes attributes of a person
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

    #sets the first name, from a value in main.py
    def set_first_name(self, first_name):
        self.first_name = first_name
    #gets the first name, and returns it
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

    #the tickets have no value in the beginning, they get it
    #assigned in the lottery_function.py
    def set_tickets(self, tickets):
        self.tickets = tickets
    #return the value from the lottery_function.py
    def get_tickets(self):
        return self.tickets


