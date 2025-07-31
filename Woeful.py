"""
-------------------------------------------------- Link for the challenge: https://codeforces.com/contest/1712/problem/B -----------------------------

You are given a positive integer n.

Find any permutation p of length n such that the sum lcm(1,p1)+lcm(2,p2)+…+lcm(n,pn) is as large as possible.

Here lcm(x,y) denotes the least common multiple (LCM) of integers x and y.

A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). Description of the test cases follows.

The only line for each test case contains a single integer n (1 ≤ n ≤ 10^5).

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case print n integers p1, p2, …, pn — the permutation with the maximum possible value of lcm(1,p1) + lcm(2,p2) +…+ lcm(n,pn).

If there are multiple answers, print any of them.

Input:
2
1
2

Output:
1
2 1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    result = []
    if n % 2 == 0:
        for i in range(1, n + 1, 2):
            result.extend([i + 1, i])
    else:
        result.append(1)
        for i in range(2, n, 2):
            result.extend([i + 1, i])
        #if n % 2 != 0 and n > 1:
        #    result.append(n)
    print(*result)