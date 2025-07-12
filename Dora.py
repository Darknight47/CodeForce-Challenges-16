"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2007/A -----------------------------------

Dora has a set s containing integers. In the beginning, she will put all integers in [l,r] into the set s. 
That is, an integer x is initially contained in the set if and only if l≤x≤r. 
Then she allows you to perform the following operations:

Select three distinct integers a, b, and c from the set s, such that gcd(a,b)=gcd(b,c)=gcd(a,c)=1†.
Then, remove these three integers from the set s.
What is the maximum number of operations you can perform?

† Recall that gcd(x,y) means the greatest common divisor of integers x and y.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The only line of each test case contains two integers l and r (1 ≤ l ≤ r ≤ 1000) — the range of integers in the initial set.

Output
For each test case, output a single integer — the maximum number of operations you can perform.

Input:
8
1 3
3 7
10 21
2 8
51 60
2 15
10 26
1 1000

Output:
1
1
3
1
2
3
4
250
"""
from math import gcd

cases = int(input())

def are_pairwise_coprime(a, b, c):
    return gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1

for _ in range(cases):
    l, r = map(int, input().split())
    arr = list(range(l, r + 1))
    used = set()
    ans = 0

    i = l
    while i + 2 <= r:
        a, b, c = i, i + 1, i + 2
        if a not in used and b not in used and c not in used:
            if are_pairwise_coprime(a, b, c):
                used.update([a, b, c])
                ans += 1
                i += 3  # skip to next candidate triple
            else:
                i += 1  # slide window forward
        else:
            i += 1
    print(ans)