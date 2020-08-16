def wo_rec_fact(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    print(fact)
    return

def w_rec_fact(n):
    if n <= 1:
        return 1
    return n * w_rec_fact(n-1)
    
def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact

def rec_factorial(n):
    if n <= 1:
        return 1
    return n*rec_factorial(n-1) 

if __name__ == '__main__':
    print(rec_factorial(5))
    # print(factorial(5))
    # wo_rec_fact(5)
    # print(w_rec_fact(7))