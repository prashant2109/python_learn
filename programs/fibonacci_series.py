#output = 0 1 1 2 3 5 8 13 21 34


def without_rec(n):
    a = 0
    b = 1
    while a < 50:
        print(a)
        a, b = b, a + b
    return 

def with_rec(n):
    if n <= 1:
        return n
    return (with_rec(n-1) + with_rec(n-2))

def fibo(n):
    a, b = 0, 1
    lst = []
    while a < n:
        lst.append(a)
        a, b = b, a+b
    return lst

def fibo_rec(n):
    if n <= 1:
        return n
    return (fibo_rec(n-1)+fibo_rec(n-2))

if __name__ == '__main__':
    # print(fibo(15))
    # without_rec(50)

    for ele in range(8):
        #print(with_rec(ele))
        print(fibo_rec(ele))