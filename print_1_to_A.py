def ass(A):
    if(A==1):
        print(1)
        return 1
    ass(A-1)
    print(A)
A=int(input())
ass(A)

"""
Input 1:
A = 10
Output 1:
1 2 3 4 5 6 7 8 9 10


Input 2:
A = 5
Output 2:
1 2 3 4 5
"""


        
        
