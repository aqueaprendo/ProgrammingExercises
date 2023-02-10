cuadrado = lambda int: int*int
print(cuadrado(3))
print(cuadrado(4))

my_list = [1,2,3,4,5]
odd = [ i for i in my_list if i % 2 != 0]
print(odd)

odd = list(filter(lambda x: x % 2 != 0,my_list))

print(odd)
my_list = [1,2,3,4,5]
odd = list(filter(lambda  x: (x*x)>=0,my_list))
print(odd)

ml = [1,2,3,4,5]
ml = [i*i for i in ml ]
print(ml)

ml = [1,2,3,4,5]
ml = list(map(lambda x: x**2,ml))
print(ml)
#####
from functools import reduce


ml = [1,2,3,4,5]
ml = reduce(lambda x,y: x+y,ml)
print(ml)