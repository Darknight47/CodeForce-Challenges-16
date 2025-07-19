"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1566/B ------------------------------------

A binary string is a string that consists of characters 0 and 1.

Let MEX of a binary string be the smallest digit among 0 , 1, or 2 that does not occur in the string. 
For example, MEX of 001011 is 2, because 0 and 1 occur in the string at least once, MEX of 1111 is 0, because 0 and 2 do not occur in the string and 0<2.

A binary string s is given. You should cut it into any number of substrings such that each character is in exactly one substring. 
It is possible to cut the string into a single substring — the whole string.

A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) 
characters from the beginning and several (possibly, zero or all) characters from the end.

What is the minimal sum of MEX of all substrings pieces can be?

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — 
the number of test cases. Description of the test cases follows.

Each test case contains a single binary string s (1 ≤ |s| ≤ 10^5).

It's guaranteed that the sum of lengths of s over all test cases does not exceed 10^5.

Output
For each test case print a single integer — the minimal sum of MEX of all substrings that it is possible to get by cutting s optimally.

Input:
6
01
1111
01100
101
0000
01010

Output:
1
0
2
1
1
2
"""
cases = int(input())
for _ in range(cases):
    s = input()
    if '0' not in s:
        print(0)
    else:
        blocks = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '0':
                blocks += 1
                while i < n and s[i] == '0':
                    i += 1
            else:
                i += 1
        print(min(blocks, 2))