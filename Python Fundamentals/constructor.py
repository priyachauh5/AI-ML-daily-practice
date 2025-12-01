# class Student:
#     subject="python"
#     college="Sinhgad"
#     year="4th year"

# stud1=Student()
# print(stud1.subject, stud1.college, stud1.year)

# class Student:
#     def __init__(self, name, cgpa):
#         self.name=name
#         self.cgpa=cgpa

# stud1= Student("Priya", 9.52)
# stud2= Student("Urvashi", 8.4)

# print(stud1.name)
# print(stud1.cgpa)

# class Student:
#     def __init__(self, name, cgpa):
#         self.name=name  #instance attributes
#         self.cgpa=cgpa

#     def get_cgpa(self):
#         return self.cgpa

# stud1= Student("Priya", 9.52)
# stud2= Student("Urvashi", 8.4)

# print(stud1.name)
# print(stud1.cgpa)
# print(f"{stud1.name} has cgpa = {stud1.get_cgpa()}")


class Student:
    college_name="ABC college" # class

    def __init__(self, name, cgpa):
        self.name=name  #instance attributes
        self.cgpa=cgpa


stud1= Student("Priya", 9.52)
# stud2= Student("Urvashi", 8.4)

print(stud1.name)
print(Student.college_name)
# print(f"{stud1.name} has cgpa = {stud1.get_cgpa()}")

#instance>class attritube