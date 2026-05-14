# 1833B-Restore-the-Weather

**Problem:** [1833B-Restore-the-Weather](https://codeforces.com/contest/1833/problem/B)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

You are given an array a containing the weather forecast for Berlandia for the last n days. That is, a_i — is the estimated air temperature on day i (1 ≤ i ≤ n).

You are also given an array b — the air temperature that was actually present on each of the days. However, all the values in array b are mixed up. 

Determine which day was which temperature, if you know that the weather never differs from the forecast by more than k degrees. In other words, if on day i the real air temperature was c, then the equality |a_i - c| ≤ k is always true.

For example, let an array a = [1, 3, 5, 3, 9] of length n = 5 and k = 2 be given and an array b = [2, 5, 11, 2, 4]. Then, so that the value of b_i corresponds to the air temperature on day i, we can rearrange the elements of the array b so: [2, 2, 5, 4, 11]. Indeed: 

 
-  On the 1st day, |a_1 - b_1| = |1 - 2| = 1, 1 ≤ 2 = k is satisfied; 
-  On the 2nd day |a_2 - b_2| = |3 - 2| = 1, 1 ≤ 2 = k is satisfied; 
-  On the 3rd day, |a_3 - b_3| = |5 - 5| = 0, 0 ≤ 2 = k is satisfied; 
-  On the 4th day, |a_4 - b_4| = |3 - 4| = 1, 1 ≤ 2 = k is satisfied; 
-  On the 5th day, |a_5 - b_5| = |9 - 11| = 2, 2 ≤ 2 = k is satisfied.


**Input**

The first line of input data contains a single integer t (1 ≤ t ≤ 10⁴) — the number of test cases.

The description of the test cases follows.

The first line of each test case contains two integers n (1 ≤ n ≤ 10⁵) and k (0 ≤ k ≤10⁹) — the number of days and the maximum difference between the expected and actual air temperature on each day.

The second line of each test case contains exactly n integers — elements of array a (-10⁹ ≤ a_i ≤ 10⁹).

The third line of each test case contains exactly n integers — elements of array b (-10⁹ ≤ b_i ≤ 10⁹).

It is guaranteed that the sum of n over all test cases does not exceed 10⁵, and that the elements of array b can always be rearranged so that the equality |a_i - b_i| ≤ k is true for all i.


**Output**

On a separate line for each test case, output exactly n numbers — the values of air temperature on each of the days in the correct order. 

If there is more than one answer — output any of them.


**Example**

**Input**

```
3
5 2
1 3 5 3 9
2 5 11 2 4
6 1
-1 3 -2 0 -5 -1
-4 0 -1 4 0 0
3 3
7 7 7
9 4 8
```

**Output**

```
2 2 5 4 11
0 4 -1 0 -4 0
8 4 9
```
