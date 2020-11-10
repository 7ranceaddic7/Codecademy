last_semester_gradebook = [
  ("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = list(zip(subjects, grades))

subjects.append("computer science")
grades.append(100)

gradebook.append(("visual arts", 93))

full_gradebook = last_semester_gradebook + gradebook

print(subjects)
print(grades)
print(gradebook)

print(full_gradebook)