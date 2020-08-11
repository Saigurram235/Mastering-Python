#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # x = [0] * (n + 1)
    # for i in range(len(queries)):
    #     for j in range(queries[i][0]-1, queries[i][1]):
    #         x[j] = x[j] + queries[i][2]

    # return max(x)
    array = [0] * (n + 1)

    for a, b, k in queries:
        array[a - 1] += k
        array[b] -= k
        print(array)
    print(array)
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        print(running_count)
        max_value = max(max_value, running_count)
        print(max_value)
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()