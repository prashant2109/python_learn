#     *
#    * *
#   * * *
#  * * * *
# * * * * *

def star_prob(num):
    for i in range(num):
        for j in range(num-i-1):
            print(end=" ")
        for j in range(i+1):
            print('*', end=" ")
        print()

def star_rev(num):
    for i in range(num, 0, -1):
        for j in range(num-i):
            print(end=" ")
        for j in range(i):
            print('*', end=" ")
        print()

def diamond(num):
    for i in range(num):
        print(' '*(num-i-1)+'*'*(i+1))
    for j in range(num-1, 0, -1):
        print(' '*(num-j)+'*'*(j))



if __name__ == '__main__':
    # star_prob(6)
    # star_rev(5)
    diamond(5)
    

