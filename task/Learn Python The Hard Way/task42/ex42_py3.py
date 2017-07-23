#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name):
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        # person has a pet of some kind
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Haibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon

harry = Haibut()

