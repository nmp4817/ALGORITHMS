# # Dynamic Programming Python implementation of Coin Change problem
# def count(S, m, n):
#     # We need n+1 rows as the table is consturcted in bottom up
#     # manner using the base case 0 value case (n = 0)
#     table = [[0 for x in range(m)] for x in range(n+1)]
#     print table
#     # Fill the enteries for 0 value case (n = 0)
#     for i in range(m):
#         table[0][i] = 1
#     print table
#     # Fill rest of the table enteries in bottom up manner
#     for i in range(1, n+1):
#         for j in range(m):
#             # Count of solutions including S[j]
#             if i==3 and j == 1:
#                 print i - S[j]
#             x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
#             # Count of solutions excluding S[j]
#             y = table[i][j-1] if j >= 1 else 0
 
#             # total count
#             table[i][j] = x + y
#     print table
#     return table[n][m-1]


# # Driver program to test above function
# arr = [1, 2, 3]
# m = len(arr)
# n = 4
# print(count(arr, m, n))


# Dynamic Programming Python implementation of Coin 
# Change problem
#!/bin/python

import sys

def getWays(n, c):
    # Complete this function
    mem = [0 for k in range(n+1)]
 
    # Base case (If given value is 0)
    mem[0] = 1 
    
    # picked coin
    for i in range(0,m):
        for j in range(c[i],n+1):
            mem[j] += mem[j-c[i]]
        
    return mem[n]
 
if __name__ == '__main__':
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = map(long, raw_input().strip().split(' '))
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    ways = getWays(n, c)
    print ways
