"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1405/A ------------------------------

A permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Let p be any permutation of length n. We define the fingerprint F(p) of p as the sorted array of sums of adjacent elements in p. More formally,

F(p)=sort([p1+p2,p2+p3,…,pn−1+pn]).

For example, if n=4 and p=[1,4,2,3], then the fingerprint is given by F(p)=sort([1+4,4+2,2+3])=sort([5,6,5])=[5,5,6].

You are given a permutation p of length n. 
Your task is to find a different permutation p′ with the same fingerprint. Two permutations p and p′ are considered different if there is some index i such that pi≠p′i.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 668). Description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100)  — the length of the permutation.

The second line of each test case contains n integers p1,…,pn (1 ≤ p(i) ≤ n). It is guaranteed that p is a permutation.

Output
For each test case, output n integers p′1,…,p′n — a permutation such that p′≠p and F(p′)=F(p).

We can prove that for every permutation satisfying the input constraints, a solution exists.

If there are multiple solutions, you may output any.

Input:
3
2
1 2
6
2 1 6 5 4 3
5
2 4 3 1 5

Output:
2 1
1 2 5 6 3 4
3 1 5 2 4
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    for i in range(sze - 1, 0, -2):
        print(arr[i], arr[i - 1], end=' ')
    if(sze % 2 == 1):
        print(arr[0], end=' ')
    print()