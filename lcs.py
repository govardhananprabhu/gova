"""Question:
You are given with two strings,consider the characters in strings are dancers,they can
have all posiible pairs from string,you task is to find the length longest common pairs
from given strings.
Note:you shoud not use any list to solve it by dynamic programing

Input description
First line has str1 and second line has str2

Output description
print the length

Test cases

Input
ABCDEF
AVGTFE
Output
2

Input
ACD
ADC
Output
2

Input
AGGTAB
GXTXAYB
Output
4

Input
ABCDGH
AEDFHR
Output
3

Input
ABCD
EFGH
Output
0

Solution:"""
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1);
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 


 
X = input()
Y = input()
print(lcs(X , Y, len(X), len(Y)))
