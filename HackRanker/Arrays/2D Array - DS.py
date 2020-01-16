# A = []
# for arr_i in range(6):
#     arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     A.append(arr_t)
#
# smax = -9 * 7
#
# for row in range(len(A) - 2):
#     for column in range(len(A[row]) - 2):
#         tl = A[row][column]
#         tc = A[row][column + 1]
#         tr = A[row][column + 2]
#         mc = A[row + 1][column + 1]
#         bl = A[row + 2][column]
#         bc = A[row + 2][column + 1]
#         br = A[row + 2][column + 2]
#         s = tl + tc + tr + mc + bl + bc + br
#         smax = max(s, smax)
#
# print(smax)



import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):


    smax = -9 * 7

    for row in range(len(arr) - 2):
        for column in range(len(arr[row]) - 2):
            tl = arr[row][column]
            tc = arr[row][column + 1]
            tr = arr[row][column + 2]
            mc = arr[row + 1][column + 1]
            bl = arr[row + 2][column]
            bc = arr[row + 2][column + 1]
            br = arr[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax = max(s, smax)
    return smax

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

    # board = []
    # for i in range(6):
    #     board.append([int(x) for x in input().split()])
    # i, j = 0, 0
    # m = sum([board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j + 1], board[i + 2][j], board[i + 2][j + 1],
    #          board[i + 2][j + 2]])
    # for i in range(4):
    #     for j in range(4):
    #         acc = sum([board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j + 1], board[i + 2][j],
    #                    board[i + 2][j + 1], board[i + 2][j + 2]])
    #         m = max(m, acc)
    # print(m)




    '''
    1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
    '''