Shopee has N software engineers. Shopee accommodates them by arranging N tables on a 1D plane. However, many people raise concerns that the work environment is too noisy. To mitigate this issue, Shopee decides to group the engineers into K groups. A group is a non-overlapping segment of contiguous engineers. Shopee will then put dividers between the groups.

 

The noise value of a group is defined by the following function:

noise(l,r) = (\sum\limits_{i=l}^{r} A _{i})*(r - l +1)


Let:

noise(l,r) be the noise value of a group consisting of the l-th engineer up to the r-th engineer.

A _{i} be the noise factor of the i-th engineer.

 

Shopee wants to minimize the total noise value. Please help Shopee to find the minimum total noise value possible.

 

**Input**

The first line of input contains 2 integers: N, K (1 <= N <= 10 000, 1 <= K <= min(N,100) representing the number of engineers and the number of groups respectively. The next line contains N integers: A_{i} (1 <= A_{i} <= 10 000) representing the noise factor of the i-th engineer.

 

**Output**

Output in a line an integer representing the minimum total noise value possible.

Sample Input:
4 2
1 3 2 4

Sample Output:
20



**Explanation**

There are 3 ways to put the divider:

1.  1 | 3 2 4
    Noise = (1 * 1) + (9 * 3) = 28
2.  1 3 | 2 4
    Noise = (4 * 2) + (6 * 2) = 20
3.  1 3 2 | 4
    Noise = (6 * 3) + (4 * 1) = 22
    
We can see that from all the possibilities, 20 is the minimum total noise value.



Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB