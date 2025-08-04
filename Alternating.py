"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2010/A --------------------------------

You are given a sequence of integers. Output the alternating sum of this sequence. In other words, output a1−a2+a3−a4+a5−…. 
That is, the signs of plus and minus alternate, starting with a plus.

Input
The first line of the test contains one integer t (1 ≤ t ≤ 1000) — the number of test cases. Then follow t test cases.

The first line of each test case contains one integer n (1 ≤ n ≤ 50) — the length of the sequence. The second line of the test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100).

Output
Output t lines. For each test case, output the required alternating sum of the numbers.

Input:
4
4
1 2 3 17
1
100
2
100 100
5
3 1 4 1 5

Output:
-15
100
0
10
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = arr[0]
    for i in range(1, sze):
        if(i % 2 == 1):
            ans -= arr[i]
        else:
            ans += arr[i]
    print(ans)