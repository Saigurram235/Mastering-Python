#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, q):
    ar = []
    for i in range(n):
        ar.append([])
    lastans = 0
    st = []
    for i in range(len(q)):
        if q[i][0] == 1:
            ar[ (q[i][1] ^ lastans) % n ].append(q[i][2])
        else:
            st.append(ar[ (q[i][1] ^ lastans) % n ][q[i][2] % len(ar[ (q[i][1] ^ lastans) % n ])])
            print(ar[ (q[i][1] ^ lastans) % n ][q[i][2] % len(ar[ (q[i][1] ^   lastans) % n ])])
            lastans = ar[ (q[i][1] ^ lastans) % n ][q[i][2] % len(ar[ (q[i][1] ^ lastans) % n ])]
    return st


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    # for i in range(len(queries)):
    #     print(queries[i][2])
    result = dynamicArray(n, queries)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()


# https://www.hackerrank.com/challenges/dynamic-array/problem