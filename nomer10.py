#jawaban nomer 10
gameboard = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def print_game_board(gameboard):
    for i in range(len(gameboard)):
        if i % 3 == 0 and i != 0:  
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(gameboard[0])):
            if j % 3 == 0 and j :
                print(" | ", end="")
            
            if j == 8:
                print(gameboard[i][j])
            else:
                print(str(gameboard[i][j]) + " ", end="")

def find_empty_sqaure(gameboard):
    for i in range(len(gameboard)):
        for j in range(len(gameboard[0])):
            if gameboard[i][j] == 0:
                return (i, j)  
    return None

def followsTheRules(gameboard, number, position):

    for i in range(len(gameboard[0])):
        if gameboard[position[0]][i] == number and position[1] != i:
            return False

    for i in range(len(gameboard)):
        if gameboard[i][position[1]] == number and position[0] != i:
            return False

    x_axis = position[1] // 3
    y_axis = position[0] // 3

    for i in range(y_axis*3, y_axis*3 + 3):
        for j in range(x_axis * 3, x_axis*3 + 3): 
            if gameboard[i][j] == number and (i,j) != position:
                return False

    return True  

def puzzleSolver(gameboard): #Recursion Function

    if not find_empty_sqaure(gameboard):
        return True
    
    else:
        row, col = find_empty_sqaure(gameboard)

    for i in range(1, 10):
        if followsTheRules(gameboard, i, (row, col)):
            gameboard[row][col] = i 
            if puzzleSolver(gameboard):
                return True
            
            gameboard[row][col] = 0

    return False 





print("_________________________UNSOLVED SUDOKU PUZZLE_______________________________")
print_game_board(gameboard)
puzzleSolver(gameboard)
print("___________________________THE SOLUTION_______________________________________")
print_game_board(gameboard)
