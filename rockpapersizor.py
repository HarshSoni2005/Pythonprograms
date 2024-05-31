import random

print("Enter 1 for choosing Rock \nEnter 2 for choosing Paper \nEnter 3 for choosing Scissors\n")

while True:
    user_ch = int(input("Enter your choice: "))
    if user_ch == 1:
        user_choice = "Rock"
    elif user_ch == 2:
        user_choice = "Paper"
    elif user_ch == 3:
        user_choice = "Scissors"
    else:
        print("Invalid choice! Try again.")
        continue

    print(f"You have chosen {user_choice}!\n")
    print("Now it's the computer's turn to choose.\n")

    cp_ch = random.randint(1, 3)
    if cp_ch == 1:
        cp_choice = "Rock"
    elif cp_ch == 2:
        cp_choice = "Paper"
    else:
        cp_choice = "Scissors"

    print(f"Computer's choice: {cp_choice}!\n")
    print("Now it's Time to Play")

    if user_choice == cp_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and cp_choice == "Scissors") or \
         (user_choice == "Paper" and cp_choice == "Rock") or \
         (user_choice == "Scissors" and cp_choice == "Paper"):
        print("User wins!!")
    else:
        print("Computer wins!!")

    play_again = input("Do you want to play again (Y/N)? ").upper()
    if play_again == 'N':
        break

print("Thanks for playing!")