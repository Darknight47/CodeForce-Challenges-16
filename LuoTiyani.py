"""
---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1825/A ---------------------------------

LuoTianyi gives you a palindrome† string s, and she wants you to find out the length of the longest non-empty subsequence‡ of s which is not a palindrome string. 
If there is no such subsequence, output −1 instead.

†
 A palindrome is a string that reads the same backward as forward. For example, strings "z", "aaa", "aba", "abccba" are palindromes, but strings "codeforces", "reality", "ab" are not.

‡ A string a is a subsequence of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from b. 
For example, strings "a", "aaa", "bab" are subsequences of string "abaab", but strings "codeforces", "bbb", "h" are not.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of test cases follows.

The first and the only line of each test case contains a single string s (1≤|s|≤50) consisting of lowercase English letters — the string that LuoTianyi gives you. It's guaranteed that s is a palindrome string.

Output
For each test case, output a single integer — the length of the longest non-empty subsequence which is not a palindrome string. If there is no such subsequence, output −1.

Input:
4
abacaba
aaa
codeforcesecrofedoc
lol

Output:
6
-1
18
2
"""
cases = int(input())
for _ in range(cases):
    s = input()
    tempSet = set(s)
    if(len(tempSet) == 1):
        print(-1)
    else:
        print(len(s) - 1)