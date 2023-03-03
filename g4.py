#Ex 4
a = int(input())
b = int(input())
def square(begin, end):
    for i in range(begin, end+1):
        yield i*i
for num in square(a, b):
    print(num)