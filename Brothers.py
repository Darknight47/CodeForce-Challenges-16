"""
---------------------------------- Link for the challenge: https://codeforces.com/contest/2010/problem/B --------------------------------------

Three brothers agreed to meet. Let's number the brothers as follows: the oldest brother is number 1, the middle brother is number 2, and the youngest brother is number 3.

When it was time for the meeting, one of the brothers was late. Given the numbers of the two brothers who arrived on time, you need to determine the number of the brother who was late.

Input
The first line of input contains two different integers a and b (1 ≤ a, b ≤ 3, a ≠ b) — the numbers of the brothers who arrived on time. The numbers are given in arbitrary order.

Output
Output a single integer — the number of the brother who was late to the meeting.

Input:
3 1

Output:
2
"""
a, b = map(int, input().split())
arr = [a, b]
if(1 not in arr):
    print(1)
elif(2 not in arr):
    print(2)
else:
    print(3)