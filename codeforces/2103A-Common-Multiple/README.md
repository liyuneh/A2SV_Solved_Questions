# 2103A-Common-Multiple

**Problem:** [2103A-Common-Multiple](https://codeforces.com/contest/2103/problem/A)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

You are given an array of integers a_1, a_2, …, a_n. An array x_1, x_2, …, x_m is beautiful if there exists an array y_1, y_2, …, y_m such that the elements of y are distinct (in other words, y_i≠ y_j for all 1 ≤ i  \lt  j ≤ m), and the product of x_i and y_i is the same for all 1 ≤ i ≤ m (in other words, x_i⋅ y_i = x_j⋅ y_j for all 1 ≤ i  \lt  j ≤ m).

Your task is to determine the maximum size of a subsequence^{\text{∗}} of array a that is beautiful.

^{\text{∗}}A sequence b is a subsequence of a sequence a if b can be obtained from a by the deletion of several (possibly, zero or all) element from arbitrary positions.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.  

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the array a.

The second line of each test case contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n) — the elements of array a.

Note that there are no constraints on the sum of n over all test cases.


**Output**

For each test case, output the maximum size of a subsequence of array a that is beautiful.


**Example**

**Input**

```
3
3
1 2 3
5
3 1 4 1 5
1
1
```

**Output**

```
3
4
1
```


**Note**

In the first test case, the entire array a = [1, 2, 3] is already beautiful. A possible array y is [6, 3, 2], which is valid since the elements of y are distinct, and 1⋅ 6 = 2⋅ 3 = 3⋅ 2.

In the second test case, the subsequence [3, 1, 4, 5] is beautiful. A possible array y is [20, 60, 15, 12]. It can be proven that the entire array a = [3, 1, 4, 1, 5] is not beautiful, so the maximum size of a subsequence of array a that is beautiful is 4.
