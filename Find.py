"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1608/A -------------------------------

Given n, find any array a1,a2,…,an of integers such that all of the following conditions hold:

1≤ai≤109 for every i from 1 to n.

a1<a2<…<an

For every i from 2 to n, ai isn't divisible by ai−1

It can be shown that such an array always exists under the constraints of the problem.

Input
The first line contains the number of test cases t (1≤t≤100). Description of the test cases follows.

The only line of each test case contains a single integer n (1≤n≤1000).

It is guaranteed that the sum of n over all test cases does not exceed 10^4.

Output
For each test case print n integers a1,a2,…,an — the array you found. If there are multiple arrays satisfying all the conditions, print any of them.

Input:
3
1
2
7

Output:
1
2 3
111 1111 11111 111111 1111111 11111111 111111111
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    if(n == 1):
        print(1)
    elif(n == 2):
        print(2, 3)
    else:
        print(*range(2, n + 2))