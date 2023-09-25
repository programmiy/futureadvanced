from itertools import permutations
#순열 permutations
arr =[x for x in range(0,4)]


for i in permutations(arr,4):
    print(i)
    
