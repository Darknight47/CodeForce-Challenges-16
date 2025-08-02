"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1701/B -----------------------------

Recall that a permutation of length n is an array where each element from 1 to n occurs exactly once.

For a fixed positive integer d, let's define the cost of the permutation p of length n as the number of indices i (1≤i<n) such that pi⋅d=pi+1.

For example, if d=3 and p=[5,2,6,7,1,3,4], then the cost of such a permutation is 2, because p2⋅3=p3 and p5⋅3=p6.

Your task is the following one: for a given value n, find the permutation of length n and the value d with maximum possible cost (over all ways to choose the permutation and d). 
If there are multiple answers, then print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases.

The single line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5).

The sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print the value d in the first line, and n integers in the second line — the permutation itself. 
If there are multiple answers, then print any of them.

Input:
2
2
3

Output:
2
1 2
3
2 1 3
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    used = set()
    perm = []
    d = 2
    for i in range(1, num + 1):
        if i not in used:
            chain = []
            val = i
            while val <= num and val not in used:
                chain.append(val)
                used.add(val)
                val *= d
            perm.extend(chain)
    
    print(2)
    print(*perm)