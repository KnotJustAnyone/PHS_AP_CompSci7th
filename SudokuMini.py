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
      self.board = puzzle

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
        pass

    def check_win(self):
        # Checks if the whole board is filled out correctly
        # Returns True if the puzzle is solved
        pass

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

#Emiri outlined the code and found the general aspects of what to put
#Angelleen wrote it all out on the program and definied all the variables
