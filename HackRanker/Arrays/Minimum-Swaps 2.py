
# n = int(input())
# arr = list(map(int, input().split()))
# swaps = 0
#
# for i in range(0, n - 1):
#     while arr[i] != i + 1:
#         t = arr[arr[i] - 1]
#         arr[arr[i] - 1] = arr[i]
#         arr[i] = t
#         swaps += 1
#
# print(swaps)

'''
5
2 3 4 1 5

'''


import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr,n):
    swaps=0
    for i in range(0, n - 1):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            swaps += 1

    return swaps

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr,n)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
