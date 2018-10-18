# python 3
import os
import sys
import time
import random
if __name__ == "__main__":
    n = list(map(int , input().rstrip().split()))
    arr = list(map(int , input().rstrip().split()))

    def function(arr , n):
        value = 0
        for i in range(len(arr)):
            for j in range(i+1 , len(arr)):
                if (arr[i] + arr[j])%n[1]==0:
                    value = value + 1
                else:
                    pass
        return value
    print(function(arr , n))
        
    
    
                    
                
    
    

