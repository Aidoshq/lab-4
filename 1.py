def it(max):
    x = 1
    while x<=max:
        yield x*x
        x+=1

n = int(input())
for x in it(n):
  print(x)