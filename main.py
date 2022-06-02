import random
while True:
    possible_options= ["R", "P", "S"]

    # User Section
    print("Options are: \"R\" for Rock, \"P\" for Paper, and \"S\" for Scissors")

    while True:
        user_turn = str(input("Enter an option: "))  

        if user_turn == "R":
            option = 'Rock'
            break
        elif user_turn == "P":
            option = 'Paper'
            break
        elif user_turn == "S":
            option = 'Scissors'
            break 
        else:
            print("Your input is invalid") 



    print("Your choice is: " + option)    
    #CPU Section         
    print("Now its computer turn.......")
    CPU_turn = random.choice(possible_options) 

    if CPU_turn == "R":
        choice_name = 'Rock'
    elif CPU_turn == "P":
        choice_name = 'Paper'
    elif CPU_turn == "S":
        choice_name == 'Scissor'
    print("CPU's choice is: " + choice_name)

    # Rock vs Paper vs Scissors
    if user_turn == CPU_turn:
        print(f"Both players selected {user_turn}. It's a tie!")
    elif user_turn == "R":
        if CPU_turn == "S":
            print("Rock crushes CPU, You win!")
        else:
            print("Paper covers you, You lose.")
    elif user_turn == "P":
        if CPU_turn == "R":
            print("Paper covers CPU, You win!")
        else:
            print("Scissors cuts you, You lose.")
    elif user_turn == "S":
        if CPU_turn == "P":
            print("Scissors cuts CPU, You win!")
        else:
            print("Rock crushes you, You lose.")

    print("Do you want to play again? (Y/N)")
    Replay = input()

    # Replay option
    if Replay == 'n' or Replay == 'N':
        print("Thanks for playing")
        break 

    
