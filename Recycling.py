"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2128/A ----------------------------------------

In the recycling center, there are n trash bags, the i-th bag has a weight of ai. At each second, two actions will happen successively:

First, you must choose a trash bag and destroy it. It will cost 1 coin if the weight of the trash bag is strictly greater than c, and it will cost 0 coins otherwise.
Then, the weight of each remaining trash bag will get multiplied by two.
What is the minimum number of coins you have to spend to get rid of all trash bags?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The first line of each test case contains two integers n and c (1 ≤ n ≤ 30, 1 ≤ c ≤ 10^9).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the weight of each trash bag.

Output
For each test case, you must output a single integer — the minimum number of coins you have to spend to destroy all trash bags.

Input:
4
5 10
10 4 15 1 8
3 42
1000000000 1000000000 1000000000
10 30
29 25 2 12 15 42 14 6 16 9
10 1000000
1 1 1 1 1 1 1 1 1 864026633

Output:
2
3
6
1
"""
cases = int(input())
for _ in range(cases):
    sze, c = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    count = 0
    mul = 1
    for i in range(sze - 1, -1 , -1):
        temp = arr[i] * mul
        if(temp > c):
            count += 1
        else:
            mul *= 2
    print(count)