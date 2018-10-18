#birthday chocolate

import os
import sys
import time
import random
if __name__ == "__main__":
    
    n = int(input())
    arr = list(map(int , input().rstrip().split()))
    month_date = list(map(int , input().rstrip().split()))
    
    if len(arr) == n and len(month_date) == 2:
        
        value = 0
        i = 0 
        
        cont = True
        
        while cont:
            
            list1 = arr[i:i+month_date[1]]
            if i + month_date[1] <= len(arr):
                sum = 0
                for a in list1:
                    
                    sum = sum + a
                    
                if sum == month_date[0]:
                    value = value + 1
                else:
                    pass
                
            if i + month_date[1]> len(arr):
                cont = False
            else:
                cont = True
            i = i + 1
    
        print(value)    
    else:
        pass
    
    
                
        
        

