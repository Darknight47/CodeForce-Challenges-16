"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1684/B ----------------------------

You are given three positive integers a, b, c (a<b<c). 
You have to find three positive integers x, y, z such that:

x mod y = a,
y mod z = b,
z mod x = c.

Here p mod q denotes the remainder from dividing p by q. 
It is possible to show that for such constraints the answer always exists.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10000) — the number of test cases. Description of the test cases follows.

Each test case contains a single line with three integers a, b, c (1 ≤ a < b < c ≤ 10^8).

Output
For each test case output three positive integers x, y, z (1≤x,y,z≤10^18) such that xmody=a, ymodz=b, zmodx=c.

You can output any correct answer.

Input:
4
1 3 4
127 234 421
2 7 8
59 94 388

Output:
12 11 4
1063 234 1484
25 23 8
2221 94 2609
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    arr = sorted([a, b, c])
    a = arr[0]
    b = arr[1]
    c = arr[2]
    print((a + b + c), (b + c), (c))