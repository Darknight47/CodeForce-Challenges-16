"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1711/A -----------------------------

You are given a positive integer n.

The weight of a permutation p1,p2,…,pn is the number of indices 1 ≤ i ≤ n such that i divides p(i). 
Find a permutation p1,p2,…,pn with the minimum possible weight (among all permutations of length n).

A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of permutation.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, print a line containing n integers p1,p2,…,pn so that the permutation p has the minimum possible weight.

If there are several possible answers, you can print any of them.

Input:
2
1
4

Output:
1
2 1 4 3
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    print(num, end= ' ')
    arr = list(range(1, num))
    print(*arr)