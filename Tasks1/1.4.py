import random

def determine_winner(player, computer):
    if player == computer:
        return 0  
    elif (player == 'R' and computer == 'S') or (player == 'S' and computer == 'P') or (player == 'P' and computer == 'R'):
        return 1 
    else:
        return 2  

player = input()
computer = random.choice(['R', 'S', 'P'])

print(computer)

result = determine_winner(player, computer)

if result == 0:
    print("Ничья!")
elif result == 1:
    print("Игрок побеждает!")
else:
    print("Компьютер побеждает!")
