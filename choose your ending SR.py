def playagain():
    answer = input("Play again? Y or n \n")
    if answer == "Y":
        print("OK")
        levelone()

    elif answer == "n":
        print("Goodbye!")

def levelone():
    print("Your journey begins here.")
    print("There is a fork in the road.")
    choice = input("Do you choose left or right? \n")

    if choice == "left":
        print("You lose!")
        playagain()

    elif choice == "right":
        print("Let's move on to level two.")
        leveltwo()


def leveltwo():
    print("Here we are at level two")
    choice = input("Where to? Level 3 or Level 1 \n")

    if choice == "Level 3":
        print("OK, onward!")

    elif choice == "Level 1":
        print("Back to level one we go.")
        levelone()

#Start game below
levelone()

    
