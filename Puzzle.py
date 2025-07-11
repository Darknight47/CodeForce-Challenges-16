"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1474/A ----------------------------------

In the 2022 year, Mike found two binary integers a and b of length n (both of them are written only by digits 0 and 1) that can have leading zeroes. 
In order not to forget them, he wanted to construct integer d in the following way:

he creates an integer c as a result of bitwise summing of a and b without transferring carry, so c may have one or more 2-s. 
For example, the result of bitwise summing of 0110 and 1101 is 1211 or the sum of 011000 and 011000 is 022000;
after that Mike replaces equal consecutive digits in c by one digit, thus getting d. 
In the cases above after this operation, 1211 becomes 121 and 022000 becomes 020 (so, d won't have equal consecutive digits).
Unfortunately, Mike lost integer a before he could calculate d himself. 
Now, to cheer him up, you want to find any binary integer a of length n such that d will be maximum possible as integer.

Maximum possible as integer means that 102>21, 012<101, 021=21 and so on.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains the integer n (1 ≤ n ≤ 10^5) — the length of a and b.

The second line of each test case contains binary integer b of length n. The integer b consists only of digits 0 and 1.

It is guaranteed that the total sum of n over all t test cases doesn't exceed 10^5.

Output
For each test case output one binary integer a of length n. Note, that a or b may have leading zeroes but must have the same length n.

Input:
5
1
0
3
011
3
110
6
111000
6
001011

Output:
1
110
100
101101
101110
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    ans = []
    lastDigit = None

    for i in range(sze):
        temp = int(s[i])

        if(temp + 1 != lastDigit):
            ans.append('1')
            lastDigit = temp + 1
        elif(temp + 0 != lastDigit):
            ans.append('0')
            lastDigit = temp + 0
        else:
            ans.append('0')
            lastDigit = temp
    print(''.join(ans))