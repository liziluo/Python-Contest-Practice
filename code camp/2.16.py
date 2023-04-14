list1=["shakespeare-hamlet-25.txt",
"shakespeare-othello-47.txt",
"shakespeare-romeo-48.txt",
"dickens-david-626.txt",
"dickens-oliver-627.txt"
"dickens-christmas-125.txt"
"twain-adventures-27.txt"
"twain-adventures-28.txt"
"twain-prince-30.txt"]
list2=["test.txt"]
from collections import Counter
from itertools import combinations, product




def part1(list1):
    number=0
    wholebook=[]
    bookn=len(list1)
    for i  in list1:
        currentbook=[]
        with open(i) as f:
            for line in f:
                for word in line.split():
                    currentbook.append(word)
        
        number+=len(currentbook)
        wholebook.append(set(currentbook))
    print("Of the %d words found in this collection of %d books"%(number,bookn))
    for j in combinations(wholebook,2):
        print(j)
part1(list2)

def part2(list2):
    currentbook=[]
    flat_list=[]
    for x  in list2:
        with open(x) as f:
            for line in f:
                for word in line.split():
                    currentbook.append(word)
        Counter1 = Counter(currentbook)
    mostuse=Counter1.most_common(1)
    print('%s "%s” used %d times'%(x,mostuse[0][0],mostuse[0][1]))
part2(list2)



####word_counter = {}
##for word in currentbook:
##     if word in currentbook:
##         word_counter[word] += 1
##     else:
##        word_counter[word] = 1
