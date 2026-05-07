# 2227D-Palindromex

**Problem:** [2227D-Palindromex](https://codeforces.com/contest/2227/problem/D)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

Yousef has given you an array a of 2n integers. Every integer x ∈ [0, n - 1] appears exactly twice in the array.

Your task is to find a subarray a_l, a_{l + 1}, …, a_r that is a palindrome^{\text{∗}} such that its \operatorname{mex}(a_l, a_{l + 1}, …, a_r)^{\text{†}} is maximized. Output this maximum possible value.

^{\text{∗}}A palindrome is a string that reads the same backward as forward, for example, strings "z", "aaa", "aba", "abccba" are palindromes, but strings "codeforces", "reality", "ab" are not.

^{\text{†}}The \operatorname{mex} (minimum excludant) of an array of integers is defined as the smallest non-negative integer which does not occur in the array. For example: 

 
-  The \operatorname{mex} of [2,2,1] is 0, because 0 does not belong to the array. 
-  The \operatorname{mex} of [3,1,0,1] is 2, because 0 and 1 belong to the array, but 2 does not. 
-  The \operatorname{mex} of [0,3,1,2] is 4, because 0, 1, 2 and 3 belong to the array, but 4 does not.


**Input**

The first line contains a single integer t (1 ≤ t ≤ 10⁴) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10⁵).

The second line of each test case contains 2n integers a_1, a_2, …, a_{2n} (0 ≤ a_i ≤ n-1). It is guaranteed that every integer in the range [0, n-1] appears exactly twice.

It is guaranteed that the sum of 2n over all test cases does not exceed 2 ⋅ 10⁵.


**Output**

For each test case, output a single integer — the maximum \operatorname{mex} of any palindromic subarray.


**Example**

**Input**

```
6
4
1 2 0 3 3 0 2 1
2
0 1 0 1
2
1 1 0 0
3
2 0 2 1 1 0
4
0 1 3 0 3 1 2 2
3
0 1 2 1 0 2
```

**Output**

```
4
2
1
1
2
3
```


**Note**

In the first test case, the only optimal subarray to choose is a[1, 8] = [1, 2, 0, 3, 3, 0, 2, 1], which is palindromic and has a \operatorname{mex} of 4.

In the second test case, one of the optimal subarrays to choose is a[2, 4] = [1, 0, 1], which is palindromic and has a \operatorname{mex} of 2.

In the third test case, we can choose a[3, 3] = [0], which is palindromic and has a \operatorname{mex} of 1. No other palindromic subarray has a \operatorname{mex} greater than 1.
