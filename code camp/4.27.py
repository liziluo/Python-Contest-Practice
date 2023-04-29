input1 = "Able was I ere I saw Elba"
#solve 2


def longlength(input1):
  dict1 = {}
  for i in input1:
    if i == " ":
      i = 123
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  candivide = 0
  odd = 0
  for item, value in dict1.items():
    if value % 2 == 0:
      candivide += value
    else:
      odd += 1
  if (odd > 0):
    return len(input1) - odd + 1
  else:
    return len(input1)


def if_palindrome(string):
  return string == string[::-1]


def longest_palindrome(input1):
  mid = ""
  right1 = ""
  left1 = ""
  dict1 = {}
  for i in input1:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  left = 0
  right = len(input1) - 1
  for i in input1:
    if left == right:
      mid = i
      break
    if dict1[input1[left]] == 1:
      left += 1
    else:
      left1 += i
      left += 1
    if dict1[input1[right]] == 1:
      right -= 1
    else:
      right1 += i
      right -= 1
  left2 = ""
  right2 = ""
  
  return (left1 + mid + right1[::-1])


print(longest_palindrome(input1))
print(longlength(input1))
