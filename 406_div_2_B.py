import sys
import math

def main():
    n,m = map(int, input().split())
    cnt = 0
    for i in range (0, m):
        k = list(map(int, input().split()))
        for i in range (1, len(k)):
            if int(k[i]*(-1)) in k:
                cnt=0
                break
            else:
                cnt=1
        if (cnt==1):
            return print("YES")
    return print("NO")

main()