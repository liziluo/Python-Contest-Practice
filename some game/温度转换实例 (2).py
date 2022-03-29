s = input ("请输入字符")
if s[-1] in ["C","c"]:
      F = (eval(s[0:-1])) * 1.8 + 32
      print("{:.2f}F".format(F))
elif s[-1] in ["F","f"]:
      C =  ( eval(s[0:-1]) - 32 ) / 1.8
      print("{:.2f}C".format(F))
else :
    print ("输入格式错误")
  
