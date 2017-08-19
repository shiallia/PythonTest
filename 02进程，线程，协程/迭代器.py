
def feb1(n):
    i = 0
    a= 0
    b=1
    while(1):
        c = a + b
        a =b
        b = c
        print(c)
        i += 1
        if(i == n):
            break

def fib2():
    i = 0
    a = 0
    b = 1
    while (b<100):
        c = a + b
        a = b
        b = c
        yield c



feb1(4)
for x in fib2():
    print(x)




