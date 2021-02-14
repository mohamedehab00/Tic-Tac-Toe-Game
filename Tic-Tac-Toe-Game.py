'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2
  1,0 | 1,1 | 1,2
  2,0 | 2,1 | 2,2
'''
N = 3

grid = []

#This function prints the grid of Tic-Tac-Toe as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks the existence of any winning row
def check_rows():
    for i in range(N):
        for j in range(N-1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] in ['X','O']:
                continue
            else:
                break
        else:
            return True

#This function checks the existence of any winning column
def check_cols():
    for i in range(N):
        for j in range(N-1):
            if grid[j][i] == grid[j+1][i] and grid[j][i] in ['X','O']:
                continue
            else:
                break
        else:
            return True

#This function checks the existence of any winning diagonal
def check_diags():
    for i in range(N-1):
        if grid[i][i] == grid[i+1][i+1] and grid[i][i] in ['X','O']:
            continue
        else:
            break
    else:
        return True
    j = 2
    for i in range(N-1):
        if grid[i][j] == grid[i+1][j-1] and grid[i][j] in ['X','O']:
            j -= 1
            continue
        else:
            break
    else:
        return True

#This function checks if row or column or diagonal is full with same characters
def check_win():
    if check_rows() or check_cols() or check_diags():
        return True
    
#This function checks if there are any empty spaces 
#if the grid has empty spaces the fuction will count them
def count_empty_spaces():
    count = 0
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == ".":
                x,y = i,j
                count+=1
    return count,x,y

#This function checks the row with this empty gap if it is a winning row 
def check_if_win_row(x,y,mark):
    if grid[x][y-1] == grid[x][y-2] and grid[x][y-1] == mark :
        return True 

#This function checks the column with this empty gap if it is a winning column 
def check_if_win_col(x,y,mark):
    if grid[x-1][y] == grid[x-2][y] and grid[x-1][y] == mark :
        return True 

#This function checks the diagonal with this empty gap if it is a winning diagonal 
def check_if_win_diag(x,y,mark):
    if ( (x == 0 or x == 2) and (y == 0 or y == 2) ) or (x == 1 and y == 1) :
        if x == y and (x == 0 or x == 2):
            if grid[x-1][y-1] == grid[x-2][y-2] and grid[x-1][y-1] == mark :
                return True
        elif x == y and x == 1 :
            if grid[x+1][y+1] == grid[x-1][y-1] and grid[x+1][y+1] == mark :
                return True
            elif grid[x-1][y+1] == grid[x+1][y-1] and grid[x-1][y+1] == mark :
                return True
        else :
            if grid[y][x] == grid[1][1] and grid[y][x] == mark :
                return True

#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    if mark == 'O' :
        mark = 'X'
    else :
        mark = 'O'

    count , x ,y = count_empty_spaces()
    if count == 1:
        if check_if_win_row(x,y,mark) or check_if_win_col(x,y,mark) or check_if_win_diag(x,y,mark):
            return False
        else :
            return True
    else :
        return False
    

#This function checks if given cell is empty or not 
def check_empty(i, j): 
    if grid[i][j] == ".":
        return True

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    if 0 <= i < N and  0 <= j < N :
        return True

#This function sets a value to a cell
def set_cell(i, j, mark):
    grid[i][j] = mark
    

#This function clears the grid
def grid_clear():
    grid.clear()

    for i in range(N):
        grid.append(["."]*N)
    

#MAIN FUNCTION
def play_game():
    print("Tic-Tac-Toe Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i, j = map(int, input('Enter the row index and column index: ').split())
        while not check_valid_position(i, j) or not check_empty(i, j):
            i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
        #Set the input position with the mark
        set_cell(i, j, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie(mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = 1 - player 


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
