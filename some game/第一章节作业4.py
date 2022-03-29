S = input()
if S[0] in ["F","f"]:
    C = (eval(S[1:]) - 32 ) / 1.8
    print("C{:.2f}".format(C))
elif S[0] in ["C","c"]:
    F = (eval(S[1:])) * 1.8 + 32
    print("F{:.2f}".format(F))
else :
    print("")
