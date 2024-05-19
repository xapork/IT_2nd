class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject: str, grade: float) -> None:
        self.subjects[subject] = grade

    def remove_subject(self, subject: str) -> None:
        if subject in self.subjects:
            del self.subjects[subject]
        else:
            print(f'Предмет {subject} отсутствует в списке предметов студента {self.name}.')

    def calc_average(self) -> float:
        if not self.subjects:
            return 0.0
        return sum(self.subjects.values()) / len(self.subjects)
        
student1 = Student("Розенгард", 17)
student1.add_subject("Линал", 5)

print(f"Средний балл студента {student1.name}: {student1.calc_average():}")

student1.remove_subject("Линал")
print(f"Средний балл студента {student1.name} после удаления предмета: {student1.calc_average():}")