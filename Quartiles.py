n = int(input())
a = input().split(' ')
arr = []
for i in range(n):
    arr.append(int(a[i]))

arr.sort()
c = (n-1)//2
c1 = (c-1)//2
c2 = ((c+1)+(n-1))//2
if n%2!=0:
    Q2 = arr[c]
    Q1 = (arr[c1]+arr[c1+1])//2
    Q3 = (arr[c2]+arr[c2+1])//2

print(Q1, Q2, Q3)