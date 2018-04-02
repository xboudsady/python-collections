import os
import random

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

# Capital indicates constants (grid tubple)
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]   

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)



def move_player(player, move):
    x, y = player   # get the player's location
    if move == "LEFT":  # if move == LEFT, x-1
        x -= 1
    if move == "RIGHT": # if move == RIGHT, x+1
        x += 1
    if move == "UP":    # if move == UP, y-1
        y -= 1
    if move == "DOWN":  # if move == DOWN, y+1
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:  # if player's x == 0, they can't move left
        moves.remove("LEFT")
    if x == 4:  # if player's x == 4, they can't move right
        moves.remove("RIGHT")
    if y == 0:  # if player's y == 0, they can't move up
        moves.remove("UP")
    if y == 4:  # if player's y == 4, they can't move down (grid limit)
        moves.remove("DOWN")
    return moves

moster, door, player = get_locations()


while True:
    valid_moves = get_moves(player)
    clear_screen()
    print("Welcome to the dungion!")
    print("You're currently in room {}".format(player)) # fill with player position
    print("You can move {}".format(", ".join(valid_moves))) # fill with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
    if move in valid_moves:
        player = move_player(player, move)
    else:
        print("\n ** Walls are hard! Don't run into them! **\n")
        continue

    # Good move? Change the player position
    # Bad move? Don't change anything!
    # On the door? They win!
    # On the monster? They lose!
    # Otherwise, loop back around
