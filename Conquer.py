"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1762/A --------------------------

An array b is good if the sum of elements of b is even.

You are given an array a consisting of n positive integers. In one operation, you can select an index i and change ai:=⌊ai2⌋. †

Find the minimum number of operations (possibly 0) needed to make a good. 
It can be proven that it is always possible to make a good.

† ⌊x⌋ denotes the floor function — the largest integer less than or equal to x. For example, ⌊2.7⌋=2, ⌊π⌋=3 and ⌊5⌋=5.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the length of the array a.

The second line of each test case contains n space-separated integers a1,a2,…,an (1 ≤ ai ≤ 10^6) — representing the array a.

Do note that the sum of n over all test cases is not bounded.

Output
For each test case, output the minimum number of operations needed to make a good.

Input:
4
4
1 1 1 1
2
7 4
3
1 2 4
1
15

Output:
0
2
1
4
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % 2 == 0:
        print(0)
    else:
        min_steps = float('inf')

        for x in arr:
            steps = 0
            original = x
            while x % 2 == original % 2:
                x //= 2
                steps += 1
            min_steps = min(min_steps, steps)
        print(min_steps)            