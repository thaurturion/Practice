import timeit
import random
import time
import array
import numpy as np

def solution_fabi(my_fun):
    #c = 0
    tmp = my_fun[0]

    i = len(my_fun) - 1

    my_fun[0] = my_fun[i]

    while i > 1:
        my_fun[i] = my_fun[i-1]
        i -= 1
        #c += 2
    my_fun[1] = tmp 

    #print(c)
    #return my_fun


def solution_luca(my_fun):
    i = 0
    tempA = my_fun[0]

    while i < len(my_fun) - 1:        
        tempB = my_fun[i+1]
        my_fun[i+1] = tempA
        tempA = tempB
        i += 1

    my_fun[0] = tempB

    #return(my_fun)
    
#def bla(arr):
#    i = 0
#def bla2(arr):


def main():
    
    #print(arr)
    #print(solutionB(arr))

    N = 5000000

    start = time.time()
    #arr = np.array([random.randint(0,1) for i in range(N)], dtype="int")
    arr = np.random.randint(2, size=N)
    #arr = array.array('i',(random.randint(0,1) for i in range(0,N))) #[random.randint(0,1) for i in range(N)]
    #arrB = copy.copy(arr)
    arrB = np.copy(arr)

    print(time.time()- start)
    print("Finished init")

    start = time.time()
    solution_fabi(arr)
    print(time.time()- start)

    start = time.time()
    solution_luca(arrB)
    print(time.time()- start)


    #print(timeit.timeit('solution_fabi(arr)', globals=globals()))
    #print(timeit.timeit('solution_luca(arr)', globals=globals()))
    #timeit.Timer("solutionA(arr)", 'gc.enable()', setup="from __main__ import test").timeit(number=10)

    #timeit.timeit(, number=100)
    #timeit.timeit("solutionB(arr)", number=100)

if __name__ == "__main__":
    main()