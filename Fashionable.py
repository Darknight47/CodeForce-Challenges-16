"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2110/A ---------------------------------

In 2077, everything became fashionable among robots, even arrays...

We will call an array of integers a fashionable if min(a)+max(a) is divisible by 2 without a remainder, where min(a) — 
the value of the minimum element of the array a, and max(a) — the value of the maximum element of the array a.

You are given an array of integers a1,a2,…,an. 
In one operation, you can remove any element from this array. Your task is to determine the minimum number of operations required to make the array a fashionable.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^3). The description of the test cases follows.

The first line of each test case contains one integer n (1 ≤ n ≤ 50) — the size of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 50) — the elements of the array a.

Output
For each test case, output one integer — the minimum number of operations required to make the array a fashionable.

Input:
6
2
5 2
7
3 1 4 1 5 9 2
7
2 7 4 6 9 11 5
3
1 2 1
2
2 1
8
8 6 3 6 4 1 1 6

Output:
1
0
2
1
1
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    
    left = arr[0]

    # Option 1: Fix min, try changing max
    for i in range(len(arr)-1, -1, -1):
        if (left + arr[i]) % 2 == 0:
            ops1 = len(arr) - 1 - i  # elements removed from right
            break
    else:
        ops1 = len(arr)

    # Option 2: Fix max, try changing min
    right = arr[-1]
    for i in range(len(arr)):
        if (arr[i] + right) % 2 == 0:
            ops2 = i  # elements removed from left
            break
    else:
        ops2 = len(arr)

    print(min(ops1, ops2))