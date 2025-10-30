import io
import sys

# Maze setup
maze = [
    "########",
    "#S     #",
    "# ###  #",
    "#   #  #",
    "# ## #G#",
    "########"
]

# Find player position
for y, row in enumerate(maze):
    if 'S' in row:
        player_x = row.index('S')
        player_y = y

def print_maze():
    for y, row in enumerate(maze):
        line = ""
        for x, ch in enumerate(row):
            if x == player_x and y == player_y:
                line += "P"  # Player
            else:
                line += ch
        print(line)

# TEST
# Capture what print_maze() prints
saved_stdout = sys.stdout
sys.stdout = io.StringIO()  # redirect print to a string

print_maze()  # ✅ call the function

# Get the printed text
output = sys.stdout.getvalue()

# Reset print back to normal
sys.stdout = saved_stdout

# Expected maze (with "P" instead of "S")
expected = """########
#P     #
# ###  #
#   #  #
# ## #G#
########
"""

# Compare and print result
if output == expected:
    print("✅ Test passed! print_maze() shows the maze correctly.")
else:
    print("❌ Test failed! Output doesn’t match expected.")
    print("Expected:")
    print(expected)
    print("Got:")
    print(output)

while True:
    print_maze()
    move = input("Move (WASD): ").lower()
    if move not in ['w', 'a', 's', 'd']:
        print("Invalid move! Use W, A, S, D keys.")
        continue

    new_x, new_y = player_x, player_y

    if move == 'w':
        new_y -= 1
    elif move == 's':
        new_y += 1
    elif move == 'a':
        new_x -= 1
    elif move == 'd':
        new_x += 1

    # Check walls
    if maze[new_y][new_x] != '#':
        player_x, player_y = new_x, new_y

    # Check goal
    if maze[player_y][player_x] == 'G':
        print_maze()
        print("You reached the goal! You win!")
        break

#Add color
from colorama import Fore, Style
print(Fore.GREEN + "P" + Style.RESET_ALL)

