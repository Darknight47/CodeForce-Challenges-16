"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1430/B -----------------------------------------

You have n barrels lined up in a row, numbered from left to right from one. Initially, the i-th barrel contains ai liters of water.

You can pour water from one barrel to another. In one act of pouring, you can choose two different barrels x and y (the x-th barrel shouldn't be empty) 
and pour any possible amount of water from barrel x to barrel y (possibly, all water). You may assume that barrels have infinite capacity, so you can pour any amount of water in each of them.

Calculate the maximum possible difference between the maximum and the minimum amount of water in the barrels, if you can pour water at most k times.

Some examples:

if you have four barrels, each containing 5 liters of water, and k=1, you may pour 5 liters from the second barrel into the fourth, so the amounts of water in the barrels are [5,0,5,10], 
and the difference between the maximum and the minimum is 10;
if all barrels are empty, you can't make any operation, so the difference between the maximum and the minimum amount is still 0.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains two integers n and k (1 ≤ k < n ≤ 2⋅10^5) — the number of barrels and the number of pourings you can make.

The second line contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 10^9), where ai is the initial amount of water the i-th barrel has.

It's guaranteed that the total sum of n over test cases doesn't exceed 2⋅10^5.

Output
For each test case, print the maximum possible difference between the maximum and the minimum amount of water in the barrels, if you can pour water at most k times.

Input:
2
4 1
5 5 5 5
3 2
0 0 0

Output:
10
0
"""
cases = int(input())
for _ in range(cases):
    sze, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    arrMax = arr[-1]
    idx = 0
    tempIdx = sze - 2
    while idx < k:
        arrMax += arr[tempIdx]
        idx += 1
        tempIdx -= 1
    print(arrMax)