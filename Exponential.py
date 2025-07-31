"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1787/A --------------------------------

You are given an integer n.

Find any pair of integers (x,y) (1 ≤ x, y ≤ n) such that x^y⋅y + y^x⋅x=n.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case contains one line with a single integer n (1 ≤ n ≤ 10^9).

Output
For each test case, if possible, print two integers x and y (1 ≤ x, y ≤ n). If there are multiple answers, print any.

Otherwise, print −1.

Input:
5
3
7
42
31250
20732790

Output:
-1
-1
2 3
5 5
3 13
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    if(num % 2 == 1):
        print(-1)
    else:
        print(1, num//2)