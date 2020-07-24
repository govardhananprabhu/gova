"""Question
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0,
selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order,
then profit cannot be earned at all

Input description:
list has values
Output description:
profit earned

Test cases

Input
100 180 260 310 40 535 695
Output
865

Input
1 2 3 4 5
Output
4

Input
88 92 33 44 55 77 105 2022
Output
1993

Input
1
Output
0

Input
9 8 7 6 5 4 3 2 1
Output
0
Solution:"""

def maxProfit(price, start, end): 
	if (end <= start): 
		return 0; 
	profit = 0;
	for i in range(start, end, 1): 
		for j in range(i+1, end+1):  
			if (price[j] > price[i]):  
				curr_profit = price[j] - price[i] + maxProfit(price, start, i - 1)+ maxProfit(price, j + 1, end);  
				profit = max(profit, curr_profit); 

	return profit; 
if __name__ == '__main__': 
	price = list(map(int,input().split())) 
	n = len(price); 

	print(maxProfit(price, 0, n - 1)); 


