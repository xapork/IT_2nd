palindrome = [char.lower() for char in input() if char.isalnum()]
if palindrome == palindrome[::-1]:
    print(True)
else:
    print(False)
