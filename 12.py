import math

num = int(input())
l = int(input())
area = (num*l*l)/(4*math.tan(math.pi/num))
print(int(area))