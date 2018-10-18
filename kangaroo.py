import sys
 
def is_odd(integer):
    if integer % 2 == 0:
        return False
    else:
        return True
 
x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
 
speed_insufficient = ((v1 == v2) & (x1 != x2)) or (((x1-x2) < 0) == ((v1-v2) < 0))
 
if speed_insufficient:
    print('NO')
elif (x1 - x2) % (v2 - v1) == 0:
    print('YES')
else:
    print('NO')

