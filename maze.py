import random

def create_new_maze(width=9, height=7):
    if width % 2 == 0: width += 1
    if height % 2 == 0: height += 1

    grid = [["#" for _ in range(width)] for _ in range(height)]
    dirs = [(0,2),(0,-2),(2,0),(-2,0)]

    def carve(x,y):
        grid[y][x] = " "
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x +dx, y +dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and grid[ny][nx] == "#":
                grid[y + dy//2][x + dx//2] = " "
                carve(nx, ny)

    carve(1,1)
    
    grid[1][1] = "S"
    grid[height-2][width-2] = "G"
    
    return ["".join(row) for row in grid]

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

def restart_game():
    global player_x, player_y
    maze = create_new_maze()
    
    for y, row in enumerate(maze):
        if 'S' in row:
            player_x = row.index('S')
            player_y = y
    print("\nMaze restarted!\n")

