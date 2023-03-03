#Ex 2
N = int(input())
def even_num(n):
    for i in range(n+1):
        if i%2==0:
            yield i
print(*even_num(N), sep=', ')