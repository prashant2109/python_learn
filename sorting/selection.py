lt = [23, 4, 7, 1, 5]
for i in range(len(lt)):
    min_idx = i
    for j in range(i+1, len(lt)):
        if lt[min_idx] > lt[j]:
            min_idx = j
    lt[i], lt[min_idx] = lt[min_idx], lt[i]
print(lt)