"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1605/A ------------------------------------------------

A number a2 is said to be the arithmetic mean of two numbers a1 and a3, if the following condition holds: a1+a3=2⋅a2.

We define an arithmetic mean deviation of three numbers a1, a2 and a3 as follows: d(a1,a2,a3)=|a1+a3−2⋅a2|.

Arithmetic means a lot to Jeevan. He has three numbers a1, a2 and a3 and he wants to minimize the arithmetic mean deviation d(a1,a2,a3). 
To do so, he can perform the following operation any number of times (possibly zero):

Choose i,j from {1,2,3} such that i≠j and increment ai by 1 and decrement aj by 1

Help Jeevan find out the minimum value of d(a1,a2,a3) that can be obtained after applying the operation any number of times.

Input
The first line contains a single integer t (1 ≤ t ≤ 5000) — the number of test cases.

The first and only line of each test case contains three integers a1, a2 and a3 (1 ≤ a1, a2, a3 ≤ 10^8).

Output
For each test case, output the minimum value of d(a1,a2,a3) that can be obtained after applying the operation any number of times.

Input:
3
3 4 5
2 2 6
1 6 5

Output:
0
1
0
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    temp = (a + c) - 2*b
    if(temp % 3 == 0):
        print(0)
    else:
        print(1)