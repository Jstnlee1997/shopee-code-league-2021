It has been a year since Noel joined Shopee. Like every ordinary day, before starting daily work, Noel will go to the pantry and make a cup of coffee for himself.

A box of length N is placed next to the coffee machine in the pantry, and coffee beans of different flavors are placed in a row. Noel has his own taste preference value V for each type of coffee bean. Noel has a habit of his own, that is, every time he makes coffee, he will select coffee beans in consecutive boxes (assuming that each flavor of coffee beans is unlimited supply) and put them into the coffee machine to get a cup of mixed coffee whose taste preference value Vhat will be the average value of the chosen flavors.

A cup of mixed coffee will be called Shoffee if its taste preference value Vhat not less than K, Shoffee can quickly wake Noel up.

Noel hopes that every day he can drink a cup of Shoffee and keep himself in a good working status. Please help him calculate how many types of Shoffee can be in total.

**Input Format**

Each test case will consist of exactly 2 lines.

The first line are two positive integers N (1 <= N <= 10^5) and K(1 <= K <= 10^4) splitted by space, representing the number of coffee bean flavors, and Noel’s expectation for the coffee.

The second line contains N positive integers V(1 <= V <= 10^4) splitted by space, representing Noel’s preference value for each type of coffee bean.

**Output Format**

For each test case, please output an answer in one line representing the number of Shoffee can be in total.

Sample Input:
3 3
1 3 4

Sample Output:
3

**Explanation**
For the first test case, there are totally 6 different consecutive sequences: (1), (3), (4), (1,3), (3,4), (1,3,4), and their average values are Vhat = 1,3,4,2,3.5,8/3. 

Among these, there will be 3 numbers greater than or equal to K = 3, so the answer will be 3.



Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB