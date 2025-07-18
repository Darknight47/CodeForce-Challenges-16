"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1547/B ----------------------------------

A string s of length n (1 ≤ n ≤ 26) is called alphabetical if it can be obtained using the following algorithm:

first, write an empty string to s (i.e. perform the assignment s := "");
then perform the next step n times;
at the i-th step take i-th lowercase letter of the Latin alphabet and write it either to the left of the string s or to the right of the string s 
(i.e. perform the assignment s := c+s or s := s+c, where c is the i-th letter of the Latin alphabet).
In other words, iterate over the n first letters of the Latin alphabet starting from 'a' and etc. 
Each time we prepend a letter to the left of the string s or append a letter to the right of the string s. 
Strings that can be obtained in that way are alphabetical.

For example, the following strings are alphabetical: "a", "ba", "ab", "bac" and "ihfcbadeg". 
The following strings are not alphabetical: "z", "aa", "ca", "acb", "xyz" and "ddcba".

From the given string, determine if it is alphabetical.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases. Then t test cases follow.

Each test case is written on a separate line that contains one string s. 
String s consists of lowercase letters of the Latin alphabet and has a length between 1 and 26, inclusive.

Output
Output t lines, each of them must contain the answer to the corresponding test case. Output YES if the given string s is alphabetical and NO otherwise.

You can output YES and NO in any case (for example, strings yEs, yes, Yes and YES will be recognized as a positive answer).

Input:
11
a
ba
ab
bac
ihfcbadeg
z
aa
ca
acb
xyz
ddcba

Output:
YES
YES
YES
YES
YES
NO
NO
NO
NO
NO
NO
"""
cases = int(input())
for _ in range(cases):
    s = input()
    n = len(s)
    ok = True
    l, r = 0, len(s) - 1
    current = chr(ord('a') + len(s) - 1)

    while l <= r:
        if s[l] == current:
            l += 1
        elif s[r] == current:
            r -= 1
        else:
            ok = False
            break
        current = chr(ord(current) - 1)
    print("YES" if ok else "NO")