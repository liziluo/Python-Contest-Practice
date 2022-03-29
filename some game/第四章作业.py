s = 1
d = 0
while s <=966:
    if s%2 == 0:
        d -= s
    else:
        d += s 
    s += 1
print(d)
