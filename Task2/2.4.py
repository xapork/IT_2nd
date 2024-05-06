class Nikola:
    def __init__(self, name, age):
        self.name = self.process_name(name)
        self.age = age
    
    def process_name(self, name):
        if name == "Николай":
            return name
        else:
            return f"Я не {name}, а Николай"
name = input()
age = int(input())
nikola_instance = Nikola(name, age)
print(nikola_instance.name)
print(nikola_instance.age)