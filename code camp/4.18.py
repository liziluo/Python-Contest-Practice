filename='wordlist-1.txt'
def load_word_list(filename):
    with open(filename, "r") as file:
        words = [line.strip() for line in file]
    return words

#this program just find path

def find_start_and_exit(maze):
    start, exit = None, None
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '#':
                start = (x, y)
            if maze[y][x] == '$':
                exit = (x, y)
    return start, exit

def is_valid_position(maze, x, y):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] != '@'

def solve_maze(maze, words):
    start, exit = find_start_and_exit(maze)
    path = [start] ##start ==path  
    if find_path(maze, words, path, *start):
        for i, (x, y) in enumerate(path[1:], 1):
            maze[y][x] = words[len(path)-2][i-1]
        return maze
    else:
        return None

def find_path(maze, exit, x, y,path): #path record
    if x==exit[0] and y==exit[1]:
        return True
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if is_valid_position(maze, nx, ny) and (nx, ny) not in path:       
            path.append((nx,ny))
            if find_path(maze, exit, nx, ny,path)==True:
                return True
    return False
maze = [
"@@@@@@@@@@@@@@@",
"#..t.....@@@@@@",
"@@@@@@.@@@@@@@",
"@@@@@@......d.$",
"@@@@@@@@@@@@@@@",
]


def find(maze):
    start, exit = find_start_and_exit(maze)
    path=[start]
    if find_path(maze, exit,start[0],start[1],path):
      print("can find")
    else:
      print("no path exists")

def splitword(list1):
  result=[]
  record=[] #record the word that have been 
  flag=0
  for i in list1:
    current=[]
    flag=0
    x=i[0]
    y=i[1]
    x1=i[0]
    y1=i[1]
    currentuse=[]
    if [x,y] in record:
      break       
    while [x1,y1+1] in list1 and flag!=1:
      currentuse=[x1,y1+1]
      y1+=1
      record.append(currentuse)
      current.append(currentuse)
    if current:
      flag=1
    while (x1,y1-1) in list1 and flag!=1:
      currentuse=[x1,y1-1]
      y1-=1
      record.append(currentuse)
      current.append(currentuse)
    if current:
      flag=1
    while (x1+1,y1) in list1 and flag!=1:
      currentuse=[x1+1,y1]
      x1+=1
      record.append(currentuse)
      current.append(currentuse)
    if current:
      flag=1
    while (x1-1,y1) in list1 and flag!=1:
      currentuse=[x1+1,y1]
      x1-=1
      record.append(currentuse)
      current.append(currentuse)
    if current:
      current.insert(0,[x,y])
      record.pop()
      result.append(record)
  print(result)  
      
      

    

      
# def findword(list):
#   for i in range()
  

find(maze)

word_list = load_word_list("wordlist-1.txt")


solved_maze=maze

if solved_maze:
    for row in solved_maze:
        print("".join(row))
else:
    print("No path exists.")


