import random
import sys
print("'ROCK','PAPER','SCISSOR'")

wins=0
losses=0
ties=0
compmove=''

while True: #main game loop
    print("%s wins, %s losses, %s ties"%(wins,losses,ties))
    while True:#player input loop
        print("Enter your Move: \nR-Rock \nP-Paper \nS-Scissor \nQ-Quit \n")
        playermove=input()
        if playermove=='Q':
            print("You quit the game")
            sys.exit()
        if playermove=='R' or playermove=='P' or playermove=='S':
            break
        print('Type one of R, P, S and Q')

    #display player's choice
    if playermove=='R':
        print("Rock V/s")
    if playermove=='P':
        print("Paper V/S")
    if playermove=='S':
        print("Sicssor V/S")


    #display computer's choice
    randomnumber = random.randint(1,3)
    if randomnumber==1:
        compmove ='R'
        print("Rock")
    if randomnumber==2:
        compmove ='P'
        print("Paper")
    if randomnumber==3:
        compmove ='S'
        print('Scissor')
    #result
    if playermove==compmove:
        print("Game tie")
        ties=ties+1

    elif playermove=='R' and compmove=='S':
        print("you Won")
        wins=wins+1

    elif playermove=='R' and compmove=='P':
        print("you Lost")
        losses=losses+1

    elif playermove=='P' and compmove=='R':
        print("you Won")
        wins=wins+1

    elif playermove=='P' and compmove=='S':
        print("you Lost")
        losses=losses+1

    elif playermove=='S' and compmove=='R':
        print("you Lost")
        losses=losses+1

    elif playermove=='S'and compmove=='P':
        print("you Won")
        wins=wins+1