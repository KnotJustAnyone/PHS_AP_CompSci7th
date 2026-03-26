'''
There are a collection of robots on a board with squares and walls.
The robots can be moved, but when moved they will continue until stopped by hitting a wall.
The goal is to move the robots to a target location in the fewest number of stops.
'''

def menu():
    choice = None
    while choice != '2':
        choice = input("1) Start a new game\n2) Quit\n")
        if choice == '1':
            print("Game still in development")
        if choice not in ['1','2']:
            print("Invalid Choice")
    print("Thanks for Playing")

menu()