"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2042/A ---------------------------------------

There are n chests; the i-th chest initially contains ai coins. 
For each chest, you can choose any non-negative (0 or greater) number of coins to add to that chest, with one constraint: 
the total number of coins in all chests must become at least k.

After you've finished adding coins to the chests, greedy Monocarp comes, who wants the coins. He will take the chests one by one, and since he is greedy, 
he will always choose the chest with the maximum number of coins. Monocarp will stop as soon as the total number of coins in chests he takes is at least k.

You want Monocarp to take as few coins as possible, so you have to add coins to the chests in such a way that, 
when Monocarp stops taking chests, he will have exactly k coins. 
Calculate the minimum number of coins you have to add.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of two lines:

the first line contains two integers n and k (1≤n≤50; 1≤k≤10^7);

the second line contains n integers a1,a2,…,an (1≤ai≤k).

Output
For each test case, print one integer — the minimum number of coins you have to add so that, when Monocarp stops taking the chests, he has exactly k coins. 
It can be shown that under the constraints of the problem, it is always possible.

Input:
4
5 4
4 1 2 3 2
5 10
4 1 2 3 2
2 10
1 1
3 8
3 3 3

Output:
0
1
8
2
"""
cases = int(input())
for _ in range(cases):
    sze, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    tempSum = 0
    ans = 0
    for i in range(sze - 1, -1, -1):
        temp = arr[i]
        tempSum += temp
        if(tempSum == k):
            break
        elif(tempSum > k):
            tempSum -= temp
            diff = k - tempSum
            ans = diff
            break
    if(tempSum != k):
        ans = k - tempSum
    print(ans)