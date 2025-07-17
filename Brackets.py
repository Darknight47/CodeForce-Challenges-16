"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1452/C --------------------------------

You are given a string s, consisting of brackets of two types: '(', ')', '[' and ']'.

A string is called a regular bracket sequence (RBS) if it's of one of the following types:

empty string;
'(' + RBS + ')';
'[' + RBS + ']';
RBS + RBS.
where plus is a concatenation of two strings.

In one move you can choose a non-empty subsequence of the string s (not necessarily consecutive) that is an RBS, remove it from the string and concatenate the remaining parts without changing the order.

What is the maximum number of moves you can perform?

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of testcases.

Each of the next t lines contains a non-empty string, consisting only of characters '(', ')', '[' and ']'. The total length of the strings over all testcases doesn't exceed 2⋅10^5.

Output
For each testcase print a single integer — the maximum number of moves you can perform on a given string s.

Input:
5
()
[]()
([)]
)]([
)[(]

Output:
1
2
2
0
1
"""
cases = int(input())
for _ in range(cases):
    s = input()
    left_paren = left_brack = 0
    paren_count = brack_count = 0

    for ch in s:
        if ch == '(':
            left_paren += 1
        elif ch == ')':
            if left_paren > 0:
                paren_count += 1
                left_paren -= 1
        elif ch == '[':
            left_brack += 1
        elif ch == ']':
            if left_brack > 0:
                brack_count += 1
                left_brack -= 1
    print(paren_count + brack_count)        