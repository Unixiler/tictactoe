import random

# ////////////////////////////////////////////////////////////////////////
# function builds start


# who won function
def whoWon():
    # if both X and O wins
    if ((positions[6] == "X" and positions[7] == "X" and positions[8] == "X") or (positions[3] == "X" and positions[4] == "X" and positions[5] == "X") or (positions[0] == "X" and positions[1] == "X" and positions[2] == "X") or (positions[6] == "X" and positions[3] == "X" and positions[0] == "X") or (positions[7] == "X" and positions[4] == "X" and positions[1] == "X") or (positions[8] == "X" and positions[5] == "X" and positions[2] == "X") or (positions[6] == "X" and positions[4] == "X" and positions[2] == "X") or (positions[8] == "X" and positions[4] == "X" and positions[0] == "X")) and ((positions[6] == "O" and positions[7] == "O" and positions[8] == "O") or (positions[3] == "O" and positions[4] == "O" and positions[5] == "O") or (positions[0] == "O" and positions[1] == "O" and positions[2] == "O") or (positions[6] == "O" and positions[3] == "O" and positions[0] == "O") or (positions[7] == "O" and positions[4] == "O" and positions[1] == "O") or (positions[8] == "O" and positions[5] == "O" and positions[2] == "O") or (positions[6] == "O" and positions[4] == "O" and positions[2] == "O") or (positions[8] == "O" and positions[4] == "O" and positions[0] == "O")):
        print("You both won, so it's actually a tie!")
        # if X wins
    elif (positions[6] == "X" and positions[7] == "X" and positions[8] == "X") or (positions[3] == "X" and positions[4] == "X" and positions[5] == "X") or (positions[0] == "X" and positions[1] == "X" and positions[2] == "X") or (positions[6] == "X" and positions[3] == "X" and positions[0] == "X") or (positions[7] == "X" and positions[4] == "X" and positions[1] == "X") or (positions[8] == "X" and positions[5] == "X" and positions[2] == "X") or (positions[6] == "X" and positions[4] == "X" and positions[2] == "X") or (positions[8] == "X" and positions[4] == "X" and positions[0] == "X"):
        if s == "X":
            print("You won! :D")
        # if O wins
        else:
            print("AI won!")
    elif (positions[6] == "O" and positions[7] == "O" and positions[8] == "O") or (positions[3] == "O" and positions[4] == "O" and positions[5] == "O") or (positions[0] == "O" and positions[1] == "O" and positions[2] == "O") or (positions[6] == "O" and positions[3] == "O" and positions[0] == "O") or (positions[7] == "O" and positions[4] == "O" and positions[1] == "O") or (positions[8] == "O" and positions[5] == "O" and positions[2] == "O") or (positions[6] == "O" and positions[4] == "O" and positions[2] == "O") or (positions[8] == "O" and positions[4] == "O" and positions[0] == "O"):
        if s == "O":
            print("You won! :D")
        else:
            print("AI won!")
    else:
        print("It's a tie!")


# positions numbers
def showtacsNumbers():
    print("These are the numbers for the boxes:")
    print("[7]" + " " + "[8]" + " " + "[9]")
    print("[4]" + " " + "[5]" + " " + "[6]")
    print("[1]" + " " + "[2]" + " " + "[3]")

# positions
def showtacs():
    print("[" + positions[6] + "]" + " " + "[" + positions[7] + "]" + " " + "[" + positions[8] + "]")
    print("[" + positions[3] + "]" + " " + "[" + positions[4] + "]" + " " + "[" + positions[5] + "]")
    print("[" + positions[0] + "]" + " " + "[" + positions[1] + "]" + " " + "[" + positions[2] + "]")

# Player move

def playerMove():


    while True:
        m = input("Your move ")  # for example, player inputs gibberish string
        try:
            i = int(m)
            if i != 1 and i != 2 and i != 3 and i != 4 and i != 5 and i != 6 and i != 7 and i != 8 and i != 9:
                print("Invalid input!")
                continue
            elif positions[i - 1] == "X" or positions[i - 1] == "O":
                print("That box is already filled!")
                continue
            else:
                i = i - 1
                positions[i] = s
                break
        except ValueError:
            # Handle the exception
            print('Please, enter a number from 1 to 9')




# AI

def AIchoosesSymbol():
    global AImark
    AImark = " "
    if s == "X": AImark = "O"
    else:AImark = "X"



def AIplays():
    r = random.randrange(1, 10)
    while True:

        if positions[r - 1] == "X" or positions[r - 1] == "O":   # checks if box is used or not
            r = random.randrange(1, 10)
            continue
        elif positions[r - 1] == " ":
            print("AI added " + AImark + " to " + str(r))
            positions[r - 1] = AImark
            break
        else:
            print("Error!")


# End of function builds
# ////////////////////////////////////////////////////////////////////////


# The game itself
while True:
    # setup of fields
    positions = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
    s = " "

    showtacsNumbers()

    # pick a symbol
    while True:
        s = input('Play as "X" or "O" ? ')
        if s != "x" and s != "X" and s != "o" and s != "O":
            print("invalid symbol")
        elif s == "x" or s == "X":
            print("X has been picked!")
            break
        elif s == "o" or s == "O":
            print("O has been picked!")
            break
    s = s.upper()
    AIchoosesSymbol()

    # Who moves first?

    while True:
        first = input("Would you like to move first? y/n ")
        if first != "y" and first != "Y" and first != "n" and first != "N":
            print('Please, just "y" or "n"')
        elif first == "y" or first == "Y":
            showtacs()
            playerMove()
            break
        elif first == "n" or first == "N":
            break
    showtacs()
    AIplays()
    showtacs()
    playerMove()
    showtacs()
    AIplays()
    showtacs()
    playerMove()
    showtacs()
    AIplays()
    showtacs()
    playerMove()
    showtacs()
    AIplays()
    showtacs()
    playerMove()
    showtacs()
    if first == "N" or first == "n":
        AIplays()
        showtacs()
    whoWon()
    while True:
        replay = input("Replay? y/n?")
        # replay.upper() << this did not work for some reason, so added two possibilities of upper and lower cases?
        if replay != "Y" and replay != "N" and replay != "y" and replay != "n":
            print('Please just "y" or "n", replay?')
            continue
        elif replay == "N" or replay == "n":
            exit()
        elif replay == "Y" or replay == "y":
            break
    continue





