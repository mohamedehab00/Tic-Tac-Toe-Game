'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2
  1,0 | 1,1 | 1,2
  2,0 | 2,1 | 2,2
'''
N = 3
marks = ['X','O']
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
def check_rows(grid):
    for i in range(N):
        for j in range(N-1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] in ['X','O']:
                continue
            else:
                break
        else:
            return True
    return False

#This function checks the existence of any winning column
def check_cols(grid):
    for i in range(N):
        for j in range(N-1):
            if grid[j][i] == grid[j+1][i] and grid[j][i] in ['X','O']:
                continue
            else:
                break
        else:
            return True
    return False

#This function checks the existence of any winning diagonal
def check_diags(grid):
    for i in range(N-1):
        if grid[i][i] == grid[i+1][i+1] and grid[i][i] in ['X','O']:
            continue
        else:
            break
    else:
        return True
    j = N-1
    for i in range(N-1):
        if grid[i][j] == grid[i+1][j-1] and grid[i][j] in ['X','O']:
            j -= 1
            continue
        else:
            break
    else:
        return True
    return False
#This function checks if row or column or diagonal is full with same characters
def check_win():
    if check_rows(grid) or check_cols(grid) or check_diags(grid):
        return True
    else:
        return False
#This function creates a copy from the main array and set the marks to the spaces
def list_try(mark):
    temp=[]
    for row in range(N):
        l = []
        for col in range(N):
            if grid[row][col] == ".":
                l.append(mark)
            else:
                l.append(grid[row][col])
        temp.append(l)
    return temp
#This function check if there is a tie status or not
def check_tie_player(mark):
    temp = list_try(mark)
    if check_rows(temp) or check_cols(temp) or check_diags(temp):
        return False
    else:
        return True
        
#This function checks if row or column or diagonal is full with same characters
def check_tie():
    all_tie = True
    for i in range(len(marks)):
        if not check_tie_player(marks[i]):
            all_tie = False
    return all_tie
    
#This function checks if given cell is empty or not 
def check_empty(i, j): 
    if grid[i][j] == ".":
        return True
    else:
        return False

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    if 0 <= i < N and  0 <= j < N :
        return True
    else:
        return False

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
        if check_tie():
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
