"""
----------------------------------- Link for the challenge: https://codeforces.com/contest/2125/problem/B ------------------------------------

There is a robot located in the cell (a,b) of an infinite grid. Misha wants to move it to the cell (0,0). To do this, he has fixed some integer k.

Misha can perform the following operation: choose two integers dx and dy (both from 0 to k inclusive) and move the robot dx cells to the left 
(in the direction of decreasing x coordinate) and dy cells down (in the direction of decreasing y coordinate). In other words, move the robot from (x,y) to (x−dx,y−dy).

The cost of the operation is:

1, if the chosen pair (dx,dy) is used for the first time;
0, if the pair (dx,dy) has been chosen before.
Note that if dx≠dy, the pairs (dx,dy) and (dy,dx) are considered different.

Help Misha bring the robot to the cell (0,0) with minimum total cost. Note that you don't have to minimize the number of operations.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each test case contains three integers a,b, and k (1 ≤ a, b, k ≤ 10^18).

Output
For each test case, output a single integer — the minimum total cost of operations required to move the robot to the cell (0,0).

Input:
4
3 5 15
2 3 1
12 18 8
9 7 5

Output:
1
2
1
2
"""
import math
cases = int(input())
for _ in range(cases):
    a, b, k = map(int, input().split())
    if(k >= a and k >= b):
        print(1)
    else:
        temp = math.gcd(a, b)
        if((a // temp) <= k and (b // temp) <= k):
            print(1)
        else:
            print(2)