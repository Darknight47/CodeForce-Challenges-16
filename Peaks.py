"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1513/A -----------------------------

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Given two integers n and k, construct a permutation a of numbers from 1 to n which has exactly k peaks. 
An index i of an array a of size n is said to be a peak if 1<i<n and ai>ai−1 and ai>ai+1. If such permutation is not possible, then print −1.

Input
The first line contains an integer t (1 ≤ t ≤ 100) — the number of test cases.

Then t lines follow, each containing two space-separated integers n (1 ≤ n ≤ 100) and k (0 ≤ k ≤ n) — the length of an array and the required number of peaks.

Output
Output t lines. For each test case, if there is no permutation with given length and number of peaks, then print −1. 
Otherwise print a line containing n space-separated integers which forms a permutation of numbers from 1 to n and contains exactly k peaks.

If there are multiple answers, print any.

Input:
5
1 0
5 2
6 6
2 1
6 1

Output:
1 
2 4 1 5 3 
-1
-1
1 3 6 5 4 2
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    max_peaks = (n - 1) // 2
    if(max_peaks < k):
        print(-1)
    else:
        temp = list(range(1, n + 1))
        for i in range(1, 2*k, 2):
            temp[i], temp[i + 1] = temp[i + 1], temp[i]
        print(*temp)