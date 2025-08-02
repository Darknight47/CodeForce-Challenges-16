"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1930/A ------------------------------

There are 2n positive integers written on a whiteboard. Being bored, you decided to play a one-player game with the numbers on the whiteboard.

You start with a score of 0. You will increase your score by performing the following move exactly n times:

Choose two integers x and y that are written on the whiteboard.
Add min(x,y) to your score.
Erase x and y from the whiteboard.
Note that after performing the move n times, there will be no more integers written on the whiteboard.

Find the maximum final score you can achieve if you optimally perform the n moves.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 5000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the number of integers written on the whiteboard is 2n.

The second line of each test case contains 2n integers a1,a2,…,a2n (1 ≤ a(i) ≤ 10^7) — the numbers written on the whiteboard.

Output
For each test case, output the maximum final score that you can achieve.

Input:
3
1
2 3
2
1 1 2 1
3
1 1 1 1 1 1

Output:
2
2
3
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(0, len(arr), 2):
        ans += arr[i]
    print(ans)