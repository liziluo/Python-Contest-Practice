filename = "auction_06.in"

with open(filename, "r") as file:
  data = [list(map(int, line.strip().split())) for line in file]

V=data[0][1]
vouchers=[0 for i in range (len(data)-1)]
increasebenefit=[0 for i in range(len(data)-1)]
benefit=[0 for i in range(len(data)-1)]

def calculate(a, b, c):  #a benefit b other voucher / c our voucher
  pecent = c / (b + c)
  benefit = a * pecent
  return benefit
  
def max1(a, b, c):
  pecent=c/(b+c)
  pecent1=(c+1)/(b+c)
  benefitdifferent=a*pecent1-a*pecent
  return benefitdifferent



for i in range(len(data)-1):
  increasebenefit[i]=max1(data[i+1][0],data[i+1][1],vouchers[i])


 #every time update


while(V!=0):
  maxbenefit=-111
  maxpostion=-1
  maxbenefit=max(increasebenefit)
  maxpostion=increasebenefit.index(maxbenefit)
  vouchers[maxpostion]+=1
  increasebenefit[maxpostion]=max1(data[maxpostion+1][0],data[maxpostion+1][1],vouchers[maxpostion])
  V-=1



for i in range(len(benefit)):
  benefit[i]=calculate(data[i+1][0],data[i+1][1],vouchers[i])

print(sum(benefit))
