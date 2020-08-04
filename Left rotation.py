#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    c = a
    mod = d % n
    # With in runtime
    for i in range(n):
        print(str(a[(mod + i)%n]), end=" ")


# Normal

#     for i in range(0, d):
#         f = c[0]
#         # print(f)
#         for j in range(0, len(c)-1):
#             c[j] = c[j+1]
#         c[-1] = f

# for i in range(len(c)):
#     print(c[i], end=' ')


