"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1530/A -------------------------------

Let's call a number a binary decimal if it's a positive integer and all digits in its decimal notation are either 0or 1. 
For example, 1010111 is a binary decimal, while 10201 and 787788 are not.

Given a number n, you are asked to represent n as a sum of some (not necessarily distinct) binary decimals. Compute the smallest number of binary decimals required for that.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000), denoting the number of test cases.

The only line of each test case contains a single integer n (1 ≤ n ≤ 10^9), denoting the number to be represented.

Output
For each test case, output the smallest number of binary decimals required to represent n as a sum.

Input:
3
121
5
1000000000

Output:
2
5
1
"""
cases = int(input())
for _ in range(cases):
    num = input()
    print(max(num))