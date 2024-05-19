def print_file(file_name: str):
    with open(file_name, "r") as file:
        data = file.read()
        print(data)

with open("../example.txt", "w") as file:
    file.write("hello\n")
    file.write("hello\n")
    file.write("hello")
print_file("../example.txt")