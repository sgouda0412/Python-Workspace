import random


def ready():
    ready = input("Are you ready to play?: Yes or No: ")
    if ready == 'yes':
        return False
    else:
        return True

start = ready()


# Scores
myscore = 0
opponent_score = 0


# Game play
while start == False:
    # Opponents choice
    opponent = ["rock", "paper", "scissors"]
    opponent_choice = random.choices(opponent)
    opponents_go = str(opponent_choice)[2]
    # Users guess
    player = input("Please choose a weapon:\nRock\nPaper\nScissors\n")
    if player.startswith('r') and opponents_go.startswith('s'):
        print("You have chosen Rock!")
        print("You have won this round!")
        print(f"You had {player}, opponent had {opponent_choice}")
        myscore += 1
        print(f"{myscore}:{opponent_score} \n")
    elif player.startswith('s') and opponents_go.startswith('p'):
        print("You have chosen Scissors!")
        print("You have won this round!")
        print(f"You had {player}, opponent had {opponent_choice}")
        myscore += 1
        print(f"{myscore}:{opponent_score} \n")
    elif player.startswith('p') and opponents_go.startswith('r'):
        print("You have chosen Paper! ")
        print("You have won this round!")
        print(f"You had {player}, opponent had {opponent_choice}")
        myscore += 1
        print(f"{myscore}:{opponent_score} \n")
    elif opponents_go.lower() == player.lower():
        print(f"You have chosen {player}")
        print("It's a tie!")
        print(f"You had {player}, opponent had {opponent_choice}")
        print(f"{myscore}:{opponent_score} \n")
    else:
        print(f"You have chosen {player}")
        print("Opponent has won!")
        print(f"You had {player}, opponent had {opponent_choice}")
        opponent_score += 1
        print(f"{myscore}:{opponent_score} \n")
    
    start = False
        
    if myscore == 3:
        print(f"You have won! {myscore}:{opponent_score} Congrats")
        break
    elif opponent_score == 3:
        print(f"You have lost... {myscore}:{opponent_score} Unlucky")
        break

