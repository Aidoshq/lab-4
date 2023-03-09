def foo(max):
   x = 0
   while x<=max:
      yield x
      x+=2
n = int(input())
a = []
for i in foo(n):
   a.append(i)
   print(a)