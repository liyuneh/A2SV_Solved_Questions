# 2044D-Harder-Problem

**Problem:** [2044D-Harder-Problem](https://codeforces.com/contest/2044/problem/D)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

Given a sequence of positive integers, a positive integer is called a mode of the sequence if it occurs the maximum number of times that any positive integer occurs. For example, the mode of [2,2,3] is 2. Any of 9, 8, or 7 can be considered to be a mode of the sequence [9,9,8,8,7,7]. 

You gave UFO an array a of length n. To thank you, UFO decides to construct another array b of length n such that a_i is a mode of the sequence [b_1, b_2, …, b_i] for all 1 ≤q i ≤q n. 

However, UFO doesn't know how to construct array b, so you must help her. Note that 1 ≤q b_i ≤q n must hold for your array for all 1 ≤q i ≤q n.


**Input**

The first line contains t (1 ≤q t ≤q 10⁴) — the number of test cases.

The first line of each test case contains an integer n (1 ≤q n ≤q 2 ⋅ 10⁵) — the length of a.

The following line of each test case contains n integers a_1, a_2, …, a_n (1 ≤q a_i ≤q n).

It is guaranteed that the sum of n over all test cases does not exceed 2 ⋅ 10⁵.


**Output**

For each test case, output n numbers b_1, b_2, …, b_n (1 ≤q b_i ≤q n) on a new line. It can be shown that b can always be constructed. If there are multiple possible arrays, you may print any.


**Example**

**Input**

```
4
2
1 2
4
1 1 1 2
8
4 5 5 5 1 1 2 1
10
1 1 2 2 1 1 3 3 1 1
```

**Output**

```
1 2
1 1 2 2
4 5 5 1 1 2 2 3
1 8 2 2 1 3 3 9 1 1
```


**Note**

Let's verify the correctness for our sample output in test case 2.

 
-  At i = 1, 1 is the only possible mode of [1]. 
-  At i = 2, 1 is the only possible mode of [1, 1]. 
-  At i = 3, 1 is the only possible mode of [1, 1, 2]. 
-  At i = 4, 1 or 2 are both modes of [1, 1, 2, 2]. Since a_i = 2, this array is valid.
