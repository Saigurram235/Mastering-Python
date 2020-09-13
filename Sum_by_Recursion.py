def list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + list(l[1 : ])

print(list([1,2,3,4,5]))

'''
all recursive algorithms must obey three important laws:
1. A recursive algorithm must have a base case.( First, a base case is the condition that allows the algorithm to stop recursing. A base
case is typically a problem that is small enough to solve directly. In the list_sum algorithm the
base case is a list of length 1. )
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.
'''