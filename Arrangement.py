"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2027/A --------------------------------------

You are coloring an infinite square grid, in which all cells are initially white. To do this, you are given n stamps. Each stamp is a rectangle of width wi and height hi.

You will use each stamp exactly once to color a rectangle of the same size as the stamp on the grid in black. 
You cannot rotate the stamp, and for each cell, the stamp must either cover it fully or not cover it at all. 
You can use the stamp at any position on the grid, even if some or all of the cells covered by the stamping area are already black.

What is the minimum sum of the perimeters of the connected regions of black squares you can obtain after all the stamps have been used?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100).

The i-th of the next n lines contains two integers wi and hi (1 ≤ wi, hi ≤ 100).

Output
For each test case, output a single integer — the minimum sum of the perimeters of the connected regions of black squares you can obtain after all the stamps have been used.

Input:
5
5
1 5
2 4
3 3
4 2
5 1
3
2 2
1 1
1 2
1
3 2
3
100 100
100 100
100 100
4
1 4
2 3
1 5
3 2

Output:
20
8
10
400
16
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    tempW, tempH = 0, 0
    for _ in range(sze):
        w, h = map(int, input().split())
        if(w > tempW):
            tempW = w
        if(h > tempH):
            tempH = h
    print((tempH + tempW) * 2)