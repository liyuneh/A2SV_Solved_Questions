# 1832C-Contrast-Value

**Problem:** [1832C-Contrast-Value](https://codeforces.com/contest/1832/problem/C)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

For an array of integers [a_1, a_2, …, a_n], let's call the value |a_1-a_2|+|a_2-a_3|+⋯+|a_{n-1}-a_n| the contrast of the array. Note that the contrast of an array of size 1 is equal to 0.

You are given an array of integers a. Your task is to build an array of b in such a way that all the following conditions are met:

 
-  b is not empty, i.e there is at least one element; 
-  b is a subsequence of a, i.e b can be produced by deleting some elements from a (maybe zero); 
-  the contrast of b is equal to the contrast of a. 
What is the minimum possible size of the array b?


**Input**

The first line contains a single integer t (1 ≤ t ≤ 10⁴) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 3 ⋅ 10⁵) — the size of the array a.

The second line contains n integers a_1, a_2, ⋅, a_n (0 ≤ a_i ≤ 10⁹) — elements of the array itself.

The sum of n over all test cases doesn't exceed 3 ⋅ 10⁵.


**Output**

For each test case, print a single integer — the minimum possible size of the array b.


**Example**

**Input**

```
4
5
1 3 3 3 7
2
4 2
4
1 1 1 1
7
5 4 2 1 0 0 4
```

**Output**

```
2
2
1
3
```
