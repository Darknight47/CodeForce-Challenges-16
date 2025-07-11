"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1748/A ----------------------------------

You have n rectangular wooden blocks, which are numbered from 1 to n. The i-th block is 1 unit high and ⌈i2⌉ units long.

Here, ⌈x2⌉ denotes the result of division of x by 2, rounded up. For example, ⌈42⌉=2 and ⌈52⌉=⌈2.5⌉=3.

For example, if n=5, then the blocks have the following sizes: 1×1, 1×1, 1×2, 1×2, 1×3.

Find the maximum possible side length of a square you can create using these blocks, without rotating any of them. Note that you don't have to use all of the blocks.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^9) — the number of blocks.

Output
For each test case, print one integer — the maximum possible side length of a square you can create.

Input:
3
2
5
197654321

Output:
1
3
98827161
"""
import math
cases = int(input())
for _ in range(cases):
    num = int(input())
    print(math.ceil(num / 2))