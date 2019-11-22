def flipPancake(pancakes, myPancake):
    pancakeNo= 0
    while pancakeNo < myPancake:
        temp= pancakes[pancakeNo]
        pancakes[pancakeNo]= pancakes[myPancake]
        pancakes[myPancake]= temp
        pancakeNo+=1
        myPancake-=1
    return pancakes

def largestPancake(pancakes, size):
    largest=0
    for i in range(0, size):
        if pancakes[i] > pancakes[largest]:
            largest= i
    return largest

def flipAndSort(pancakes):
    pancakeSize= len(pancakes)
    while pancakeSize > 1:
        largest= largestPancake(pancakes, pancakeSize)
        if largest != pancakeSize - 1 :
            pancakes= flipPancake(pancakes, largest)
            print('pancakeSize:',pancakeSize)
            print(pancakes)
            pancakes= flipPancake(pancakes, pancakeSize-1)
            print(pancakes)
            print('-----------------------')
        pancakeSize-=1
    return pancakes


pancakeArr= [1,4,2,6,5]
print(flipAndSort(pancakeArr))