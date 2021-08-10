import random
rock = 1
paper = 2
scissors = 3
userwin = 0
compwin = 0

for gamecount in range(6):
    print(f"Round {gamecount + 1}")
    comprandom = random.randint(1,3)
    userinput = input("Rock Paper or Scissors? ")
    if(userinput == "Rock"):
        userinput = 1
    elif(userinput == "Paper"):
        userinput = 2
    elif(userinput == "Scissors"):
        userinput = 3

    if(userinput == comprandom):
        print("Tie!")
    elif(userinput == 1 and comprandom == 3):
        userwin += 1
        print("You win this round!")
    elif(userinput == 1 and comprandom == 2):
        compwin += 1
        print("You lose this round!")
    elif(userinput == 2 and comprandom == 1):
        userwin += 1
        print("You win this round!")
    elif(userinput == 2 and comprandom == 3):
        compwin += 1
        print("You lose this round!")
    elif(userinput == 3 and comprandom == 2):
        userwin += 1
        print("You win this round!")
    elif(userinput == 3 and comprandom == 1):
        compwin +=1
        print("You lose this round!")
    
    if(userwin == 3):
        print("You win!!")
        break
    elif(compwin == 3):
        print("Computer wins!!")
        break
    elif(gamecount == 5):
        if(userwin > compwin):
            print("You win!!")
            break
        elif(compwin > userwin):
            print("Computer wins!!")
            break