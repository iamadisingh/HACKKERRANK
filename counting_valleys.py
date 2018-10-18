import os
import sys
import random
if __name__ == "__main__":
    n = int(input())# number of steps
    s = input()#track of steps
    def function(s):
        level = 0 # level above or below sea level
        val = 0# if above sea level(U) val = 1 else if (D) val = -1
        if len(s) == n:
            for i in s:
                if i=="D":
                    level = level - 1
                else:
                    if level == -1:
                        val = val + 1
                    level = level + 1
        else:
            pass
        return val
    print(function(s))
