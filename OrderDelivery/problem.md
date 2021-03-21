In the parallel universe, where there are 13 months, Shopee has a 13.13 campaign. During this 13.13 campaign, Shopee gives free shipping delivery vouchers to all users who buy the item X. Shopee has N warehouses to store the item X, and each warehouse has <a href="https://www.codecogs.com/eqnedit.php?latex=W_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?W_{i}" title="W_{i}" /></a> number of item X. Each warehouse is located in a city and all cities have at most one warehouse. To serve the customers, each warehouse has its own courier delivery. The cost of the delivery from the warehouse i is <a href="https://www.codecogs.com/eqnedit.php?latex=C_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C_{i}" title="C_{i}" /></a> dollar per kilometer. Interestingly, in this parallel universe, the distance between neighboring cities is exactly one kilometer. The cities can be represented as a graph, where a node represents the city and an edge represents the road between cities, and all the cities are connected. Warehouse i is located at city <a href="https://www.codecogs.com/eqnedit.php?latex=P_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{i}" title="P_{i}" /></a>.

During the 13.13 campaign, people are very excited to buy this item X because of the free shipping discounts. As a result, there are M orders created. The i-th order contains <a href="https://www.codecogs.com/eqnedit.php?latex=K_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_{i}" title="K_{i}" /></a> number of item X, and it needs to be delivered to city <a href="https://www.codecogs.com/eqnedit.php?latex=G_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G_{i}" title="G_{i}" /></a>. To serve all the customers, multiple warehouses can be used to serve a single order. So, one order can be served by multiple warehouses.

Because of the free shipping discounts, Shopee needs to pay the delivery fee of all the orders. Your task is to help Shopee to minimize the delivery fee in this 13.13 campaign.

 

**Input Format**

The first line contains three integers N, D, and E (1<= N <= 20, 1 <= D <= N, N-1 <= E <= 200)  representing the number of cities, warehouses, and roads in this parallel universe. The next E lines contain 2 integers <a href="https://www.codecogs.com/eqnedit.php?latex=X_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{i}" title="X_{i}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=Y_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y_{i}" title="Y_{i}" /></a> (1 <= <a href="https://www.codecogs.com/eqnedit.php?latex=X_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{i}" title="X_{i}" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=Y_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y_{i}" title="Y_{i}" /></a> <= N, <a href="https://www.codecogs.com/eqnedit.php?latex=X_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{i}" title="X_{i}" /></a> != <a href="https://www.codecogs.com/eqnedit.php?latex=Y_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y_{i}" title="Y_{i}" /></a>)  which indicates that there is a road between city <a href="https://www.codecogs.com/eqnedit.php?latex=X_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?X_{i}" title="X_{i}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=Y_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Y_{i}" title="Y_{i}" /></a>. The next D line contains 3 integers Wi, Ci, and <a href="https://www.codecogs.com/eqnedit.php?latex=P_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{i}" title="P_{i}" /></a> (1 <= <a href="https://www.codecogs.com/eqnedit.php?latex=W_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?W_{i}" title="W_{i}" /></a> <= 10^9, 1 <= <a href="https://www.codecogs.com/eqnedit.php?latex=C_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C_{i}" title="C_{i}" /></a> <= 10^6, 1 <= <a href="https://www.codecogs.com/eqnedit.php?latex=P_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P_{i}" title="P_{i}" /></a> <= N)  which represents the number of item X in warehouse i and the delivery fee of warehouse i per kilometer and the location of warehouse i. The next line contains an integer M (1 <= M <= 100000) which represents the number of orders. Each of the next M lines contain two integers <a href="https://www.codecogs.com/eqnedit.php?latex=K_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_{i}" title="K_{i}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=G_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G_{i}" title="G_{i}" /></a> (1 <= <a href="https://www.codecogs.com/eqnedit.php?latex=K_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_{i}" title="K_{i}" /></a> <= 10^9, 1 <= <a href="https://www.codecogs.com/eqnedit.php?latex=G_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G_{i}" title="G_{i}" /></a> <= N, sum of all <a href="https://www.codecogs.com/eqnedit.php?latex=K_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_{i}" title="K_{i}" /></a> <= 10^9) which represent the number of item X ordered in order-i and the city of order i.


**Output Format**

Output a single integer contains the total delivery cost of all orders. It is guaranteed that Shopee can serve all the orders.

Sample Input:\
8 3 11\
1 2\
1 3\
2 3\
3 4\
4 5\
5 6\
5 7\
5 8\
4 6\
3 7\
7 8\
12 5 1\
11 10 6\
1 6 7\
3\
3 4\
4 4\
7 5\

Sample Output:\
136


Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB