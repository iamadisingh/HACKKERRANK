'''
0  1  2  3  4  5  6  7  8  
10 5  20 20 4  5  2  25 1
10 10 20 20 20 20 20 25 25
10 5  5 5   4  4  2  2  1
'''
import os
import sys
import time
import random
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int , input().rstrip().split()))
    if len(arr) == n:
        list1 = [arr[0]]
        c = 0
        for i in range(len(arr)):
            if list1[c]<arr[i]:
                list1.append(arr[i])
                c = c + 1
            else:
                pass
        list2 = [arr[0]]
        c = 0
        for i in range(len(arr)):
            if list2[c]>arr[i]:
                list2.append(arr[i])
                c = c + 1
            else:
                pass
        print(len(list1)-1 , len(list2)-1)
    else:
        pass
                
                

