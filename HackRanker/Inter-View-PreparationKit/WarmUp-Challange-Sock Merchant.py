import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()


# import sys
# from collections import defaultdict
#
# n = int(input().strip())
# c = map(int, input().strip().split(' '))
#
# d = defaultdict(int)
# for k in c:
#     d[k] += 1
#
# cnt = 0
# for ele in d.values():
#     cnt += ele // 2
#
# print(cnt)