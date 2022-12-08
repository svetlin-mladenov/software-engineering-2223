letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
board = {}
for letter in letters:
    for num in range(1, 9):
        board[letter + str(num)] = None
#Pawns
for letter in letters:
    board[letter + "7"] = "P"
    board[letter + "2"] = "P"
#Rooks
board["A1"] = "R"
board["H1"] = "R"
board["A8"] = "R"
board["H8"] = "R"

#Knights
board["B1"] = "N"
board["G1"] = "N"
board["B8"] = "N"
board["G8"] = "N"

#Bishops
board["C1"] = "B"
board["F1"] = "B"
board["C8"] = "B"
board["F8"] = "B"

#King and queen
board["D1"] = "Q"
board["E1"] = "K"
board["D8"] = "Q"
board["E8"] = "K"

whiteFirst = True
print("")
print(6 * " ", end="")
for letter in letters:
    print("  " + letter + "  ", end="")
    print(" ", end="")
print("\n")
for num in range(8, 0, -1):
    print("  " + str(num) + "   ", end="")
    for letter in letters:
        if(whiteFirst):
            if(letters.index(letter) % 2 == 1):
                print("[ " + (board[letter + str(num)] if board[letter + str(num)] else " ") + " ]", end=" ")
            else:
                print("{ " + (board[letter + str(num)] if board[letter + str(num)] else " ") + " }", end=" ")
        else:
            if(letters.index(letter) % 2 == 1):
                print("{ " + (board[letter + str(num)] if board[letter + str(num)] else " ") + " }", end=" ")
            else:
                print("[ " + (board[letter + str(num)] if board[letter + str(num)] else " ") + " ]", end=" ")
    print("\n")
    whiteFirst = not(whiteFirst)