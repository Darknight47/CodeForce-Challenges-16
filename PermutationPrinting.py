"""
---------------------------------------- Link for the challenge: https://codeforces.com/contest/1930/problem/B ----------------------------

You are given a positive integer n.

Find a permutation† p of length n such that there do not exist two distinct indices i and j (1≤i,j<n; i≠j) such that pi divides pj and pi+1 divides pj+1.

Refer to the Notes section for some examples.

Under the constraints of this problem, it can be proven that at least one p exists.

† A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array), and 
[1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output p1,p2,…,pn.

If there are multiple solutions, you may output any one of them.

Input:
2
4
3

Output:
4 1 2 3
1 2 3
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    arr = list(range(1, num + 1))
    left = 0
    right = num - 1
    result = []

    while left <= right:
        if right >= left:
            result.append(arr[right])
            right -= 1
        if left <= right:
            result.append(arr[left])
            left += 1

    print(" ".join(map(str, result)))