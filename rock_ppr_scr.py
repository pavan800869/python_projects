import random 
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def game():
    p_s = 0
    c_s = 0
    i = 0
    while i<3:
        t = ["rock", "paper", "scissors"]
        comp = random.choice(t)
        player = input("Rock, Paper, Scissors?").lower()
        print(f"You chose {player}, Computer's choice {comp}")
        if comp == player:
            print("Tie!")
        elif player== "paper":
            if comp == "rock":
                print("You Win!,")
                p_s += 1
            else:
                print("You Lost!")
                c_s += 1
        elif player=="rock":
            if comp=="scissors":
                print("You lose!")
                c_s += 1
            else:
                print("You win!")
                p_s += 1
        elif player == "scissors":
            if comp == "rock":
                print("You lose!")
                c_s += 1
            else:
                print("You win!")
                p_s += 1   
        else:
            print("Invalid input")
        i+=1
    
    print("---------------------------------")
    print("Your score is ", p_s, "Computer score is ", c_s)
        
clear_screen()
print(''' This is rock, paper, scissors game
enter you choice and play with computer
You can play this game for 3 rounds per game.''') 



game()
    


if input('Play again?[y/n] ').lower() != 'n':
            game()



    
       
                
        
        
    
    


