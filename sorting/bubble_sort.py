def bubble_sort(lt):
    n = len(lt)
    for i in range(n):
        for j in range(n-i-1):
            if lt[j] > lt[j+1]:
                lt[j], lt[j+1] = lt[j+1], lt[j]
    # print(lt)
    return lt

def bs(lt):
    n = len(lt)
    for i in range(n):
        for j in range(n-i-1):
            if lt[j] > lt[j+1]:
                lt[j], lt[j+1] = lt[j+1], lt[j]
    return lt

###########################################################################
if __name__ == '__main__':
    lt = [23, 4, 7, 1, 5]
    print(bs(lt))
    
    
