'''
There are a collection of robots on a board with squares and walls.
The robots can be moved, but when moved they will continue until stopped by hitting a wall.
The goal is to move the robots to a target location in the fewest number of stops.

#######
#  |  |  Maze format
#--####
'''
class ricochet_board:
    space = ['  ']
    vline = ['|']
    hline = ['--']
    cross = ['+']
    display_board = None #Display needs to be made on the fly
    board = None
    barriers = None

    def __init__(self):
        Wall_line = '#'*65
        Space_line = '#'+("   |")*15+'   #'
        Grid_line = '#'+'---+'*15+'---#'
        self.display_board = [Wall_line]+[Space_line,Grid_line]*15+[Space_line,Wall_line]
        self.board = [[None for _ in range(16)] for _ in range(16)]
        for i in range(2):
            for j in range(2):
                self.block_space(7+i,7+j)

    def block_space(self,y,x):
        self.board[y][x] = '#'
        for i in range(4):
            for j in range(4):
                self.display_board[3*y+i][3*x+j] = '#'

    def print_board(self):
        for row in self.board:
            print(row)
        

def menu():
    choice = None
    while choice != '2':
        choice = input("1) Start a new game\n2) Quit\nD) Debug\n")
        if choice == '1':
            print("Game still in development")
        if choice == 'D':
            test_board = ricochet_board()
            test_board.print_board()
        if choice not in ['1','2','D']:
            print("Invalid Choice")
    print("Thanks for Playing")

menu()