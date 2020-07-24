"""
Question
Assume you are a teacher now,you are given two strings first is the answer sheet and second
is the answer key,as a teacher your task is to find the number of mistakes done.

Input description:
First line has answer sheet
Second line has answer key

Output description:
print the count of mistakes

Test cases

Input
we
we
Output
0

Input
superman
supergirl
Output
4

Input
watteru
water
Output
2

Input
musup
mashup
Output
2

Input
wether
wheather
Output
2

Solution:"""
def editDistance(str1, str2, m, n): 
	if m == 0: 
		return n  
	if n == 0: 
		return m 
	if str1[m-1]== str2[n-1]: 
		return editDistance(str1, str2, m-1, n-1)
	return 1 + min(editDistance(str1, str2, m, n-1),editDistance(str1, str2, m-1, n), editDistance(str1, str2, m-1, n-1)) 


str1 = input()
str2 = input()
print(editDistance(str1, str2, len(str1), len(str2))) 


