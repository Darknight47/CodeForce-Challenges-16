"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1728/B ------------------------------

Let's define the value of the permutation p of n integers 1, 2, ..., n (a permutation is an array where each element from 1 to n occurs exactly once) as follows:

initially, an integer variable x is equal to 0;
if x<p1, then add p1 to x (set x=x+p1), otherwise assign 0 to x;
if x<p2, then add p2 to x (set x=x+p2), otherwise assign 0 to x;
...
if x < pn, then add pn to x (set x=x+pn), otherwise assign 0 to x;
the value of the permutation is x at the end of this process.
For example, for p=[4,5,1,2,3,6], the value of x changes as follows: 0,4,9,0,2,5,11, so the value of the permutation is 11.

You are given an integer n. Find a permutation p of size n with the maximum possible value among all permutations of size n. 
If there are several such permutations, you can print any of them.

Input
The first line contains one integer t (1 ≤ t ≤ 97) — the number of test cases.

The only line of each test case contains one integer n (4 ≤ n ≤ 100).

Output
For each test case, print n integers — the permutation p of size n with the maximum possible value among all permutations of size n.

Input:
3
4
5
6

Output:
2 1 3 4
1 2 3 4 5
4 5 1 2 3 6
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    p = list(range(1, n + 1))

    start = n & 1  # 1 if odd, 0 if even
    for i in range(start, n - 2, 2):
        p[i], p[i + 1] = p[i + 1], p[i]

    print(' '.join(map(str, p)))
