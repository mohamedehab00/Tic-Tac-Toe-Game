#include <bits/stdc++.h>
using namespace std;

const int N = 3;
int n_players = 2;
const char marks[2] = {'X', 'O'};
char grid[N][N];
char temp[N][N];
//This function prints the grid of Tic-Tac-Toe Game as the game progresses
void print_grid() {
    cout << "Player 1: " << marks[0] << "  vs  Player 2: " << marks[1] << "\n";
    cout << "--";
    for (int i = 0; i < N; cout << "---", i++);
    cout << "--\n";
    for (int i = 0; i < N; i++) {
        cout << "|  ";
        for (int j = 0; j < N; j++)
            cout << grid[i][j] << "  ";
        cout << "|\n";
        cout << "--";
        for (int i = 0; i < N; cout << "---", i++);
        cout << "--\n";
    }
}
bool check_row(char grid[N][N]) {
	for(int row = 0;row<N;row++){
		for(int col = 0;col < N-1;col++){
			if(grid[row][col]==grid[row][col+1] && ( grid[row][col] == 'X' || grid[row][col] == 'O' ) ){
				if(col == N-2 ){
					return true;
				}
				continue;
			}
			else{
				break;
			}		
	    }	
	}
	return false;	
}
bool check_col(char grid[N][N]) {
	for(int col = 0;col < N;col++){
		for(int row = 0; row < N-1; row++){
			if(grid[row][col]==grid[row+1][col] && ( grid[row][col] == 'X' || grid[row][col] == 'O' ) ){
				if(row == N-2 ){
					return true;
				}
				continue;
			}
			else{
				break;
			}
		}
			
	}
	return false;	
}
bool check_diag(char grid[N][N]) {
	for(int i = 0 ; i < N-1 ; i++ ){
		if(grid[i][i]==grid[i+1][i+1] && ( grid[i][i] == 'X' || grid[i][i] == 'O' )){
			if(i == N-2 ){
				return true;
			}
			continue;	
		}
		else{
			break;
		}
	}
	for(int i = N-1,j=0 ; i > 0,j<N-1 ; i--,j++ ){
		if(grid[i][j]==grid[i-1][j+1] && ( grid[i][j] == 'X' || grid[i][j] == 'O' )){
			if(i == 1 ){
				return true;
			}
			continue;	
		}
		else{
			break;
		}
	}
	return false;
}
//This function checks if the game has a win state or not
bool check_win() {
	if(check_row(grid)||check_col(grid)||check_diag(grid)){
		return true;
	}
	return false;
}
//This function copy the main array(grid) to a temporary array(temp) and replace empty spaces with marks
void arr_try(char mark){
	for(int i = 0;i<N;i++){
		for(int j = 0;j<N;j++){
			if(grid[i][j]==' '){
				temp[i][j] = mark;
			}else{
				temp[i][j] = grid[i][j];
			}
		}		
	}
}
//This function checks if the game has a tie state or not for the given mark
bool check_tie_player(char mark) {
	arr_try(mark);
	if(check_row(temp)||check_col(temp)||check_diag(temp)){
		return false;
	}
	return true;	
}
//This function checks if the game has a tie state or not
bool check_tie() {
    bool all_tie = true;
    for (int i = 0; i < n_players; i++)
        if (!check_tie_player(marks[i]))
            all_tie = false;
    return all_tie;
}
//This function checks if given cell is empty or not 
bool check_empty(int i, int j) {
	if(grid[i][j]==' '){
		return true;
	}
	else{
		return false;
	}
}
//This function checks if given position is valid or not 
bool check_valid_position(int i, int j) {
	if(( i >= 0 && i < N ) && ( j >= 0 && j < N )){
		return true;
	}
	else{
		return false;
	}
}
//This function sets the given mark to the given cell
void set_cell(int i, int j, char mark) {
	grid[i][j] = mark;
}
//This function clears the game structures
void grid_clear() {
	for(int i = 0 ; i<N ; i++){
		for(int j = 0 ; j<N ; j++){
			grid[i][j] = ' ';
		}
	}
}
//This function reads a valid position input
void read_input(int &i, int &j) {
	cout << "Enter the row index and column index: ";
	cin >> i >> j;
    while (!check_valid_position(i, j) || !check_empty(i, j)) {
		cout << "Enter a valid row index and a valid column index: ";
		cin >> i >> j;
	}
}
//MAIN FUNCTION
void play_game() {
    cout << "Tic-Tac-Toe Game!\n";
    cout << "Welcome...\n";
    cout << "============================\n";
    bool player = 0;
    while (true) {
        //Prints the grid
        print_grid();
        //Read an input position from the player
        cout << "Player " << marks[player] << " is playing now\n";
        int i, j;
		read_input(i, j);
        //Set the player mark in the input position
        set_cell(i, j, marks[player]);
        //Check if the grid has a win state
        if (check_win()) {
            //Prints the grid
            print_grid();
			//Announcement of the final statement
            cout << "Congrats, Player " << marks[player] << " is won!\n";
            break;
        }
        //Check if the grid has a tie state
        if (check_tie()) {
            //Prints the grid
            print_grid();
			//Announcement of the final statement
            cout << "Woah! That's a tie!\n";
            break;
        }
        //Player number changes after each turn
        player = 1 - player;
    }
}
int main() {
    while (true) {
    	grid_clear();
    	play_game();
    	char c;
    	cout << "Play Again [Y/N] ";
    	cin >> c;
    	if (c != 'y' && c != 'Y')
    		break;
    }
}
