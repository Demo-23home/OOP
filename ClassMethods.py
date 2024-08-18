class Student:
    count: int = 0
    total_gpa: float = 0

    def __init__(self, name: str, gpa: float) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_details(self) -> str:
        return f"{self.name} {self.gpa}"

    # CLASS METHOD
    @classmethod
    def get_count(cls) -> str:
        return f"Total # of students is {cls.count}"

    # CLASS METHOD  
    @classmethod
    def get_AVG_GPA(cls) -> float:
        if cls.count == 0:
            return 0
        else:
            return cls.total_gpa / cls.count


std1 = Student("Zeyad", 3.3)
std2 = Student("Mohammed", 3.5)
std3 = Student("Tarek", 4.0)


print(Student.get_count())
print(Student.get_AVG_GPA())
