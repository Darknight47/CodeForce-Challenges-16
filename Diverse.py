"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1144/A --------------------------------------

A string is called diverse if it contains consecutive (adjacent) letters of the Latin alphabet and each letter occurs exactly once. 
For example, the following strings are diverse: "fced", "xyz", "r" and "dabcef". The following string are not diverse: "az", "aa", "bad" and "babc". Note that the letters 'a' and 'z' are not adjacent.

Formally, consider positions of all letters in the string in the alphabet. These positions should form contiguous segment, i.e. they should come one by one without any gaps. 
And all letters in the string should be distinct (duplicates are not allowed).

You are given a sequence of strings. For each string, if it is diverse, print "Yes". Otherwise, print "No".

Input
The first line contains integer n (1 ≤ n ≤ 100), denoting the number of strings to process. 
The following n lines contains strings, one string per line. Each string contains only lowercase Latin letters, its length is between 1 and 100, inclusive.

Output
Print n lines, one line per a string in the input. The line should contain "Yes" if the corresponding string is diverse and "No" if the corresponding string is not diverse. 
You can print each letter in any case (upper or lower). For example, "YeS", "no" and "yES" are all acceptable.

Input:
8
fced
xyz
r
dabcef
az
aa
bad
babc

Output:
Yes
Yes
Yes
Yes
No
No
No
No
"""
cases = int(input())
for _ in range(cases):
    s = input()
    sortedStr = sorted(s)
    temp = int(ord(sortedStr[0]))
    ok = True
    for i in range(1, len(sortedStr)):
        diff = int(ord(sortedStr[i])) - temp
        if(diff > 1 or diff == 0):
            ok = False
            break
        else:
            temp = int(ord(sortedStr[i]))
    print("YES" if ok else "NO")