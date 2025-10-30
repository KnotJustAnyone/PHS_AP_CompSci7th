maze = [
    "########",
    "#S     #",
    "# ###  #",
    "#   #  #",
    "# ## #G#",
    "########"
]

# Player position
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
        
#Clean screen on each turn
import os
os.system('cls' if os.name == 'nt' else 'clear')
maze = [list(row) for row in maze]



