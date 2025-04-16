'''
Player 1 and 2 
Player 1 = X
Player 2 = O'''

square = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def checkwinner():
    if (square[1] == square[2]) and (square[2] == square[3]):
        return 1
    elif (square[1] == square[5]) and (square[5] == square[9]):
        return 1
    elif (square[1] == square[4]) and (square[4] == square[7]):
        return 1
    elif (square[2] == square[5]) and (square[5] == square[8]):
        return 1
    elif (square[4] == square[5]) and (square[5] == square[6]):
        return 1
    elif (square[7] == square[8]) and (square[8] == square[9]):
        return 1
    elif (square[3] == square[6]) and (square[6] == square[9]):
        return 1
    elif (square[3] == square[5]) and (square[5] == square[7]):
        return 1
    elif (square[1] != '1' and square[2] != '2' and square[3] != '3' and square[4] != '4' and 
          square[5] != '5' and square[6] != '6' and square[7] != '7' and square[8] != '8' and 
          square[9] != '9'):
        return 0
    else:
        return -1
    

def printBoard():
    print("\nPlayer 1 - 'X' \t Player 2 - 'O'\n")
    print(f"    {square[1]}   |   {square[2]}   |   {square[3]}  ")
    print(f"--------|-------|-------")
    print(f"    {square[4]}   |   {square[5]}   |   {square[6]}   ")
    print(f"--------|-------|-------")
    print(f"    {square[7]}   |   {square[8]}   |   {square[9]}   \n")


if __name__ == "__main__":
    player = 1
    i = -1
    print("Welcome to Tic Tac Toe Game")
    while(i == -1):
        printBoard()
        player = 1 if (player % 2) else 2
        choice = int(input("Player {0}, pls enter your choice : ".format(player)))

        mark = 'X' if (player == 1) else 'O'

        if choice == 1 and square[1] == '1':
            square[1] = mark
        elif choice == 2 and square[2] == '2':
            square[2] = mark
        elif choice == 3 and square[3] == '3':
            square[3] = mark
        elif choice == 4 and square[4] == '4':
            square[4] = mark
        elif choice == 5 and square[5] == '5':
            square[5] = mark
        elif choice == 6 and square[6] == '6':
            square[6] = mark
        elif choice == 7 and square[7] == '7':
            square[7] = mark
        elif choice == 8 and square[8] == '8':
            square[8] = mark
        elif choice == 9 and square[9] == '9':
            square[9] = mark
        else:
            print("INVALID!!!!")
            player -= 1
            
        i = checkwinner()
        player += 1

    printBoard()
    if(i == 1):
        player -= 1
        print("--> Player {0} won the Game.\n".format(player))
    else:
        print("--> Game is draw\n")



        