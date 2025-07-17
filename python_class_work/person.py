from person import Person
from problem import Problem


class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.problems = []

    def add_problem(self, problem: Problem):
        self.problems.append(problem)


p1 = Person("John", 22, "Male")
