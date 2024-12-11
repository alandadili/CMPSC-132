class Person:
    def __init__(self, id, name, height):
        self.id = id
        self.name = name
        self.height = height

class Student(Person):
    def __init__(self, id, name, height, student_id, major):
        super().__init__(id, name, height)
        self.student_id = student_id
        self.major = major

# Example usage:
student1 = Student("P123", "John Doe", 175, "S001", "Computer Science")
print("Student ID:", student1.student_id)
print("Name:", student1.name)
print("Height:", student1.height)
print("Major:", student1.major)