"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2126/A ------------------------------

You are given an integer x. 
You need to find the smallest non-negative integer y such that the numbers x and y share at least one common digit. 
In other words, there must exist a decimal digit d that appears in both the representation of the number x and the number y.

Input
The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains one integer x (1 ≤ x ≤ 1000).

Output
For each test case, output one integer y — the minimum non-negative number that satisfies the condition.

Input:
5
6
96
78
122
696

Output:
6
6
7
1
6
"""
cases = int(input())
for _ in range(cases):
    numStr = sorted(input())
    print(numStr[0])