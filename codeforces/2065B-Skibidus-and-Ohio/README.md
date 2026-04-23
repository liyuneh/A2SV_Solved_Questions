# 2065B-Skibidus-and-Ohio

**Problem:** [2065B-Skibidus-and-Ohio](https://codeforces.com/contest/2065/problem/B)

**time limit per test:** 1 second

**memory limit per test:** 256 megabytes

---

Skibidus is given a string s that consists of lowercase Latin letters. If s contains more than 1 letter, he can:

 
-  Choose an index i (1 ≤q i ≤q |s| - 1, |s| denotes the current length of s) such that s_i = s_{i+1}. Replace s_i with any lowercase Latin letter of his choice. Remove s_{i+1} from the string. 
Skibidus must determine the minimum possible length he can achieve through any number of operations.


**Input**

The first line contains an integer t (1 ≤q t ≤q 100) — the number of test cases.

The only line of each test case contains a string s (1 ≤q |s| ≤q 100). It is guaranteed s only contains lowercase Latin letters.


**Output**

For each test case, output an integer on the new line, the minimum achievable length of s.


**Example**

**Input**

```
4
baa
skibidus
cc
ohio
```

**Output**

```
1
8
1
4
```


**Note**

In the first test case, Skibidus can:

 
-  Perform an operation on i = 2. He replaces s_2 with b and removes s_3 from the string. Then, s becomes bb. 
-  Perform an operation on i = 1. He replaces s_1 with b and removes s_2 from the string. Then, s becomes b. 
-  Because s only contains 1 letter, Skibidus cannot perform any more operations. 
Therefore, the answer is 1 for the first test case.

In the second test case, he cannot perform an operation on any index. Therefore, the answer is still the length of the initial string, 8.
