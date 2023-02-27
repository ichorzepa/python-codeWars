# https://www.codewars.com/kata/54da5a58ea159efa38000836
# 6 kyu
import numpy as np
def find_it(seq):
    x = np.array(seq)
    uniqal = np.unique(x)
    for uniq in uniqal:
        if (seq.count(uniq) % 2) != 0: 
            return uniq 
        else:
            continue

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))