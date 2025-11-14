class Sudoku4x4:
    def __init__(self):
        # This is where we make the 4x4 board using a list of lists
        # At the beginning all the cells are 0 (empty)
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def load_puzzle(self, puzzle):
        # Loads a starting puzzle (4x4 grid with numbers and zeros)
        # puzzle is supposed to be a list of lists with the numbers
        pass

    def test_load_puzzle(self, puzzle):
        game = Sudoku4x4()
        puzzle = [
            [1, 2, 3, 4],
            [4, 1, 2, 3],
            [3, 4, 1, 2],
            [2, 3, 4, 1]
        ]
        game.load_puzzle(puzzle)
        assert game.board == puzzle

    def print_board(self):
        # Could use this for testing or when playing in the console
        for character in range(len(self.board[0]) * 4 + 1): # Horizontal line at the top
                print('—',end='')
        for row in self.board:
            toPrint = '\n| ' # Starts a new line
            for value in row: # Adds a vertical line between each value
                toPrint += str(value)
                toPrint += ' | ' 
            print(toPrint)
            for character in range(len(row) * 4 + 1): # Adds a horizontal line across each row
                print('—',end='')
        pass

    def check_move(self, row, col, num):
        # Checks if placing 'num' at (row, col) is allowed
        # Has to follow Sudoku rules (no repeats in row, column, or box)
        pass

    def place_number(self, row, col, num):
        # Actually puts the number on the board if the move is okay
        # Might return True or False depending on if it worked
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return False
        if self.board[row][col] != 0:
            return False
        if not self.is_valid_move(row, col, num):
            return False
        self.board[row][col] = num
        return True

    def check_win(self):
        # Checks if the whole board is filled out correctly
        # Returns True if the puzzle is solved
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                if num == 0 or not self.is_valid_move(row, col, num):
                    return False
        return True


    def reset_board(self):
        # Clears the board or maybe resets it to the original puzzle
        pass

    def get_hints(self, row, col):
        # This would give possible numbers that can go in a spot
        # Might help a player who is stuck
        pass

    def auto_solve(self):
        # Tries to solve the puzzle on its own (probably using backtracking)
        pass
    def test_auto_solve_sudoku_mini():
        board = [
            [1, 0, 0, 4],
            [0, 0, 1, 0],
            [0, 3, 0, 0],
            [2, 0, 0, 0]
        ]
        solved = auto_solve(board)
    
        # Check rows
        for row in solved:
            assert set(row) == {1, 2, 3, 4}
    
        # Check columns
        for col in range(4):
            column_vals = {solved[row][col] for row in range(4)}
            assert column_vals == {1, 2, 3, 4}

#Emiri outlined the code and found the general aspects of what to put
#Angelleen wrote it all out on the program and definied all the variables
