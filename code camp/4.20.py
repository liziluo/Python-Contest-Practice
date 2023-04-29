import random

# Define the board size and ships
BOARD_SIZE = 10
SHIPS = {
  'Aircraft Carrier': 5,
  'Battleship': 4,
  'Submarine': 3,
  'Destroyer': 3,
  'Patrol Boat': 2
}

ship=[  'Aircraft Carrier',  'Battleship',  'Submarine',   'Destroyer',  'Patrol Boat']
# Initialize the board and ship positions
board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
ship_positions = {}

# def place():


# Function to place a ship on the board
def place_ship(ship, size):
  while True:
    # Choose a random starting position and orientation for the ship
    row = random.randint(0, BOARD_SIZE - 1)
    col = random.randint(0, BOARD_SIZE - 1)
    horizontal = random.choice([True, False])
    positions = []

    # Check if the ship can be placed in the chosen position
    if horizontal:
      if col + size <= BOARD_SIZE:
        overlap = False
        for i in range(size):
          if board[row][col + i] != '.':
            overlap = True
            break
        if not overlap:
          for i in range(size):
            board[row][col + i] = ship[0]
            positions.append((row, col + i))
          return positions
    else:
      if row + size <= BOARD_SIZE:
        overlap = False
        for i in range(size):
          if board[row + i][col] != '.':
            overlap = True
            break
        if not overlap:
          for i in range(size):
            board[row + i][col] = ship[0]
            positions.append((row + i, col))
          return positions


# Place all the ships on the board
for ship, size in SHIPS.items():
  positions = place_ship(ship, size)
  ship_positions[ship] = positions


# Function to print the board
def print_board(player):
  print("Player " + str(player) + "'s board:")
  print("  " +
        " ".join([chr(c) for c in range(ord('A'),
                                        ord('A') + BOARD_SIZE)]))
  for i in range(BOARD_SIZE):
    print(str(i) + " " + " ".join(board[i]))


# Print the starting board for each player
print_board(1)
# print_board(2)

# Initialize game variables
player1_hits = set()
player1_misses = set()
player2_hits = set()
player2_misses = set()
turn = 1
play1 = 0
shipexist = [0 for i in range(7)]
play1usedattrack = set()


# Function to check if a ship has been sunk
def check_sunk(ship_positions, hits):
  for ship, positions in ship_positions.items():
    if all(pos in hits for pos in positions):
      print(ship + " has been sunk!")


# Game loop
while True:
  for i in range(1, 6):
    if shipexist[i] != 0:
      continue  #it mean that it is dead
    # Get the player's move
    currentship=ship[i]
    # printeship_positions
    print("Player " + str(i) + "'s turn")
    row = int(input("Enter a row (0-" + str(BOARD_SIZE - 1) + "): "))
    col = int(input("Enter a column (0-" + str(BOARD_SIZE - 1) + "): "))
    if (row, col) in play1usedattrack:
      print("You've already attacked that position. Try again.")
      continue
    if board[row][col] != '.':
      print("Hit!")
      player1_hits.add((row, col))
      play1usedattrack.add((row, col))
      flag = 1
      # for j in range(ship_positions[i]):
      # for j not in play1usedattrack:
      # flag=0
      # break
      # if flag==1:
      # shipexist[i]=1
      # print(ship+str(i)+ " has been sunk!")
    else:
      print("not hit")
      player1_misses.add((row, col))
      play1usedattrack.add((row, col))
