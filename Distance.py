"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1895/B ---------------------------

You are given a sequence of integers a of length 2n. You have to split these 2n integers into n pairs; 
each pair will represent the coordinates of a point on a plane. Each number from the sequence a should become the x or y coordinate of exactly one point. Note that some points can be equal.

After the points are formed, you have to choose a path s that starts from one of these points, ends at one of these points, and visits all n points at least once.

The length of path s is the sum of distances between all adjacent points on the path. 
In this problem, the distance between two points (x1,y1) and (x2,y2) is defined as |x1−x2|+|y1−y2|.

Your task is to form n points and choose a path s in such a way that the length of path s is minimized.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of testcases.

The first line of each testcase contains a single integer n (2 ≤ n ≤ 100) — the number of points to be formed.

The next line contains 2n integers a1,a2,…,a2n (0 ≤ ai ≤ 1000) — the description of the sequence a.

Output
For each testcase, print the minimum possible length of path s in the first line.

In the i-th of the following n lines, print two integers xi and yi — the coordinates of the point that needs to be visited at the i-th position.

If there are multiple answers, print any of them.

Input:
2
2
15 1 10 5
3
10 30 20 20 30 10

Output:
9
10 1
15 5
20
20 20
10 30
10 30
"""

cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    firstHalf = arr[:n]
    secondHalf = arr[n:]
    coordinates = []
    for i in range(n):
        f = firstHalf[i]
        s = secondHalf[i]
        coordinates.append((f, s))
    for j in range(n - 1):
        x1, y1 = coordinates[j]
        x2, y2 = coordinates[j + 1]
        ans += abs(x1 - x2) + abs(y1- y2)
    print(ans)
    for i in range(n):
        print(coordinates[i][0], coordinates[i][1])