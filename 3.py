def foo(max):
    x = 0
    while x<=max:
        yield x
        x+=12
n=int(input())
for i in foo(n):
    print(i)
