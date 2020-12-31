class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade.score)
        else:
            return


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


pieter.add_grade(Grade(100))
print(pieter.name)
print(pieter.year)
print(pieter.grades)

# TODO: More to do here
# Great job! You’ve created two classes and defined their interactions.
# This is object-oriented programming! From here you could:

# Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
# Write a Student method get_average() that returns the student’s average score.
# Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.
# Write your own classes to do whatever logic you want!
