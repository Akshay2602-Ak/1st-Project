import random 

user_wins = 0
computer_wins = 0

option = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue
    
    random_number = random.randint(0,2)
    # rock 0 , paper:1 , scissors:2
    computer_pick = option[random_number]
    print("Computer Picked ",computer_pick +".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won!")
        uesr_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You Won",user_wins,"times.")
print("The computer won",computer_wins,"times.")
print("Good bye :)")