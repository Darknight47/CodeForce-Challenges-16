"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1047/A ---------------------------------

Little C loves number «3» very much. He loves all things about it.

Now he has a positive integer n. 
He wants to split n into 3 positive integers a,b,c, such that a+b+c=n and none of the 3 integers is a multiple of 3. Help him to find a solution.

Input
A single line containing one integer n (3 ≤ n ≤ 10^9) — the integer Little C has.

Output
Print 3 positive integers a,b,c in a single line, such that a+b+c=n and none of them is a multiple of 3.

It can be proved that there is at least one solution. If there are multiple solutions, print any of them.

Input:
3
Output:
1 1 1
"""
num = int(input())
a = 1
b = 1
c = num - 2

if(c % 3 != 0):
    print(a, b, c)
elif((a + 1) % 3 != 0 and (c - 1) % 3 != 0 ):
    print(a + 1, b, c - 1)
elif((b + 1) % 3 != 0 and (c - 1) % 3 != 0 ):
    print(a, b + 1, c - 1)
else:
    print(a + 1, b + 1, c - 2)