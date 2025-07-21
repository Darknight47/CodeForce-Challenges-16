"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1802/A ----------------------------------------

Nikita recently held a very controversial round, after which his contribution changed very quickly.

The announcement hung on the main page for n seconds. In the ith second |ai|
th person either liked or removed the like (Nikita was lucky in this task and there are no dislikes). If ai>0, then the aith person put a like. If ai<0, 
then the person −ai removed the like. Each person put and removed the like no more than once. A person could not remove a like if he had not put it before.

Since Nikita's contribution became very bad after the round, he wanted to analyze how his contribution changed while the announcement was on the main page. 
He turned to the creator of the platform with a request to give him the sequence a1,a2,…,an. 
But due to the imperfection of the platform, the sequence a was shuffled.

You are given a shuffled sequence of a that describes user activity. You need to tell for each moment from 1 to n what 
the maximum and minimum number of likes could be on the post at that moment.

Input
The first line of input data contains one number t (1 ⩽ t ⩽ 1000) — the number of test cases.

In the first line of test case, one number is given n (1 ⩽ n ⩽ 100) — the number of seconds during which Nikita's announcement hung on the main page.

The next line contains n numbers b1,b2,b3,…,bn (1 ⩽ |bi| ⩽ n) — mixed array a. 
It is guaranteed that there exists such a permutation of b that it is a correct sequence of events described in the condition.

It is guaranteed that the sum of n for all input test cases does not exceed 10^4.

Output
For each test case, output two lines, each of which contains n numbers.

In the first line, for each test case, output the maximum number of likes that Nikita could have at the announcement at the ith second.

In the second line, for each test case, output the minimum number of likes that Nikita could have at the announcement at the ith second.

Input:
5
3
1 2 -2
2
1 -1
6
4 3 -1 2 1 -2
5
4 2 -2 1 3
7
-1 6 -4 3 2 4 1

Output:
1 2 1 
1 0 1 
1 0 
1 0 
1 2 3 4 3 2 
1 0 1 0 1 2 
1 2 3 4 3 
1 0 1 2 3 
1 2 3 4 5 4 3 
1 0 1 0 1 2 3 
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    positives = {x for x in arr if x > 0}
    negatives = {-x for x in arr if x < 0} 
    # Create ascending part
    up = list(range(1, len(positives) + 1))
    # Continue with descending part
    down = list(range(len(positives) - 1, len(positives) - len(negatives) - 1, -1))
    # Combine and stringify
    maxSequence = ' '.join(str(num) for num in up + down)
    print(maxSequence)

    # Create '1 0' pairs for each negative
    neg_part = [1, 0] * len(negatives)

    # Create ascending numbers for remaining positives
    remaining_pos_count = abs(len(positives) - len(negatives))
    pos_part = list(range(1, remaining_pos_count + 1))

    # Combine both parts
    minSequence = (neg_part + pos_part)
    print(*minSequence)