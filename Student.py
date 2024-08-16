class Student:
    class_year: int = 2024
    num_students: int = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Student.num_students += 1


zeyad: Student = Student("Zeyad", 22)
Mohammed: Student = Student("Mohammed", 22)
Salama: Student = Student("Salama", 22)

print(zeyad.name)
print(Student.num_students)
