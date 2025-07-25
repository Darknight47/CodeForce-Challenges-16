"""
--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1851/B ---------------------------

You have an array of integers a of length n. You can apply the following operation to the given array:

Swap two elements a(i) and aj such that i≠j, a(i) and a(j) are either both even or both odd.
Determine whether it is possible to sort the array in non-decreasing order by performing the operation any number of times (possibly zero).

For example, let a = [7,10,1,3,2]. Then we can perform 3 operations to sort the array:

Swap a3=1 and a1=7, since 1 and 7 are odd. We get a = [1,10,7,3,2];

Swap a2=10 and a5=2, since 10 and 2 are even. We get a = [1,2,7,3,10];

Swap a4=3 and a3=7, since 3 and 7 are odd. We get a = [1,2,3,7,10].

Input
The first line of input data contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The description of the test cases follows.

The first line of each test case contains one integer n (1 ≤ n ≤ 2⋅10^5) — the length of array a.

The second line of each test case contains exactly n positive integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of array a.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output on a separate line:

YES if the array can be sorted by applying the operation to it some number of times;
NO otherwise.
You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as positive response).

Input:
6
5
7 10 1 3 2
4
11 9 3 5
5
11 3 15 3 2
6
10 7 8 1 2 3
1
10
5
6 6 4 1 6

Output:
YES
YES
NO
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    sortedAarr = sorted(arr)

    ok = True
    for original, target in zip(arr, sortedAarr):
        if(original % 2 != target % 2):
            ok = False
            break
    print("YES" if ok else "NO")