"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1316/A ----------------------------------
n students are taking an exam. The highest possible score at this exam is m. 
Let ai be the score of the i-th student. You have access to the school database which stores the results of all students.

You can change each student's score as long as the following conditions are satisfied:

All scores are integers
0 ≤ a(i) ≤ m
The average score of the class doesn't change.
You are student 1 and you would like to maximize your own score.

Find the highest possible score you can assign to yourself such that all conditions are satisfied.

Input
Each test contains multiple test cases.

The first line contains the number of test cases t (1 ≤ t ≤ 200). The description of the test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n ≤ 10^3, 1 ≤ m ≤ 10^5)  — the number of students and the highest possible score respectively.

The second line of each testcase contains n integers a1,a2,…,an (0 ≤ a(i) ≤ m)  — scores of the students.

Output
For each testcase, output one integer  — the highest possible score you can assign to yourself such that both conditions are satisfied.


Input:
2
4 10
1 2 3 4
4 5
1 2 3 4

Output:
10
5
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    first = arr[0]
    for i in range(1, n):
        first += arr[i]
    print(min(first, m))