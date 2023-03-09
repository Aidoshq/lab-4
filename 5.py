def foo(max):
    x = max
    while x>=0:
        yield x
        x-=1

n = int(input())
for i in foo(n):
    print(i)