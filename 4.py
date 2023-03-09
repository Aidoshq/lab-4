def foo(a,b):
    x = a
    while x<=b:
        yield x*x
        x+=1

bir = int(input())
eki = int(input())
for i in foo(bir,eki):
    print(i)
