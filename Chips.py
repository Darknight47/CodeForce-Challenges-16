"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/92/A ----------------------------------

There are n walruses sitting in a circle. All of them are numbered in the clockwise order: 
the walrus number 2 sits to the left of the walrus number 1, the walrus number 3 sits to the left of the walrus number 2, ..., the walrus number 1 sits to the left of the walrus number n.

The presenter has m chips. The presenter stands in the middle of the circle and starts giving the chips to the walruses starting from walrus number 1 and moving clockwise. 
The walrus number i gets i chips. If the presenter can't give the current walrus the required number of chips, then the presenter takes the remaining chips and the process ends.
Determine by the given n and m how many chips the presenter will get in the end.

Input
The first line contains two integers n and m (1 ≤ n ≤ 50, 1 ≤ m ≤ 104) — the number of walruses and the number of chips correspondingly.

Output
Print the number of chips the presenter ended up with.

Input:
4 11

Output:
0
"""
n, m = map(int, input().split())
roundTotal = n * (n + 1) // 2
fullRounds = m // roundTotal
chipsLeft = m - fullRounds * roundTotal

for i in range(1, n + 1):
    if(chipsLeft >= i):
        chipsLeft -= i
    else:
        break

print(chipsLeft)