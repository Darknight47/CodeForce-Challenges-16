"""


Kazimir Kazimirovich is a Martian gardener. He has a huge orchard of binary balanced apple trees.

Recently Casimir decided to get himself three capybaras. The gardener even came up with their names and wrote them down on a piece of paper. 
The name of each capybara is a non-empty line consisting of letters "a" and "b".

Denote the names of the capybaras by the lines a, b, and c. Then Casimir wrote the nonempty lines a, b, 
and c in a row without spaces. For example, if the capybara's name was "aba", "ab", and "bb", then the string the gardener wrote down would look like "abaabbb".

The gardener remembered an interesting property: either the string b is lexicographically not smaller than the strings a and c at the same time, 
or the string b is lexicographically not greater than the strings a and c at the same time. 
In other words, either a≤b and c≤b are satisfied, or b≤a and b≤c are satisfied (or possibly both conditions simultaneously). 
Here ≤ denotes the lexicographic "less than or equal to" for strings. 
Thus, a≤b means that the strings must either be equal, or the string a must stand earlier in the dictionary than the string b. 
For a more detailed explanation of this operation, see "Notes" section.

Today the gardener looked at his notes and realized that he cannot recover the names because they are written without spaces. 
He is no longer sure if he can recover the original strings a, b, and c, so he wants to find any triplet of names that satisfy the above property.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤500). The description of the test cases follows.

The only line of a test case contains the string s (3≤|s|≤100) — the names of the capybaras, written together. The string consists of English letters 'a' and 'b' only.

It is guaranteed that the sum of string lengths over all test cases does not exceed 500.

Output
For each test case, print three strings a , b and c on a single line, separated by spaces — names of capybaras, such that writing them without spaces results in a line s. 
Either a≤b and c≤b, or b≤a and b≤c must be satisfied.

If there are several ways to restore the names, print any of them. If the names cannot be recovered, print ":(" (without quotes).

Input:
5
bbba
aba
aaa
abba
abbb

Output:
b bb a
a b a
a a a
ab b a
a bb b
"""
cases = int(input())
for _ in range(cases):
    s = input()
    n = len(s)
    ok = False
    for i in range(1, n - 1):
        a = s[:i]
        for j in range(i + 1, n):
            b = s[i:j]
            c = s[j:]

            if(a <= b and c <= b):
                ok = True
                break
            elif(b <= a and b <= c):
                ok = True
                break
        if(ok):
            break
    if(ok):
        print(a, b, c)
    else:
        print(": (")