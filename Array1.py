#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    comps = 0

    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sorting to find the answer
    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            comps += 1
            if queue[j] > queue[j + 1]:
                temp = queue[j]
                queue[j] = queue[j + 1]
                queue[j + 1] = temp
                swaps += 1
                swaped = True

        if swaped:
            swaped = False
        else:
            break
    return swaps
    # c = []
    # d = 0
    # for i in range(min(q), len(q)+1):
    #     c.append(i)
    # for i in range(len(q)):
    #     if c[i] != q[i]:
    #         x = q.index(c[i])
    #         # print(x)
    #         z = abs(x - i)
    #         # print(z)
    #         if z <= 2:
    #             d = d + z
    #         else:
    #             print('Too chaotic')
    #             return
    # print(int(d/2))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        x = minimumBribes(q)
        print(x)
