"""
----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2130/A ----------------------------------

For a multiset T consisting of non-negative integers, we define:

sum(T) is the sum of all elements in T. For example, if T={0,1,1,3}, then sum(T)=0+1+1+3=5.

mex(T) is the smallest non-negative integer not in T. 
For example, if T={0,1,1,3}, then mex(T)=2 because 2 is the smallest non-negative integer not present in T.
You are given a multiset S of size n consisting of non-negative integers. At first, your score is 0. 
You can perform the following operations any number of times in any order (possibly zero):
Select a subset S′⊆S (i.e., S′ contains some of the elements currently in S), add sum(S′) to your score, and then remove S′ from S.
Select a subset S′⊆S, add mex(S′) to your score, and then remove S′ from S.
Find the maximum possible score that can be obtained.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^3). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50).

The second line of each test case contains n integers S1,S2,…,Sn (0 ≤ Si ≤ 50).

Output
For each test case, print a single integer — the maximum possible score that can be obtained.

Input:
2
3
0 1 1
3
1 2 3

Output:
3
6
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    for num in arr:
        if(num == 0):
            ans += 1
        else:
            ans += num
    print(ans)