def prime_no(n1, n2):
    prime_lst = []
    for i in range(n1, n2):
        if i == 2:
            prime_lst.append(i)
            continue
        for j in range(2, i//2):
            if i % j == 0:
                break
        else:
            prime_lst.append(i)
    print(prime_lst)
    return

if __name__ == '__main__':
    prime_no(2, 50)