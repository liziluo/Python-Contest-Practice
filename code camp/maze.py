#This file allows a maze to determine if there is an exit and find the fastest exit route.

startpoint = '#'
endpoint = '$'
wall = '@'


def find_start_and_exit(maze):
  start, exit = None, None
  for y in range(len(maze)):
    for x in range(len(maze[y])):
      if maze[y][x] == startpoint:
        start = (x, y)
      if maze[y][x] == endpoint:
        exit = (x, y)
  return start, exit


def is_valid_position(maze, x, y):
  return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] != wall


def find_path(maze, exit, x, y, path):  #path record
  if x == exit[0] and y == exit[1]:
    return True
  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    nx, ny = x + dx, y + dy
    if is_valid_position(maze, nx, ny) and (nx, ny) not in path:
      path.append((nx, ny))
      if find_path(maze, exit, nx, ny, path) == True:
        return True
  return False


maze = [
  "@@@@@@@@@@@@@@@",
  "#........@@@@@@",
  "@@@@@@.@@@@@@@",
  "@@@@@@........$",
  "@@@@@@@@@@@@@@@",
]


def find(maze):
  start, exit = find_start_and_exit(maze)
  path = [start]
  if find_path(maze, exit, start[0], start[1], path):
    print("can find")
    print(path)
  else:
    print("no path exists")


find(maze)



