
#Ex 5
n =int(input())
def all_num(n):
    for i in range(n, -1, -1):
        yield i
for num in all_num(n):
    print(num)