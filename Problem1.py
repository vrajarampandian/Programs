"""
You are given an array of n numbers and q queries.
For each query you have to print the floor of the expected value(mean) of the subarray from L to R.

First line contains two integers N and Q denoting number of array elements and number of queries.
Next line contains N space seperated integers denoting array elements.
Next Q lines contain two integers L and R(indices of the array).

print a single integer denoting the answer. :

1<= N ,Q,L,R <= 10^6

1<= Array elements <= 10^9

NOTE

Use Fast I/O

Problem setter : Sheldon Tauro

SAMPLE INPUT
5 3
1 2 3 4 5
1 3
2 4
2 5
SAMPLE OUTPUT
2
3
3
"""

#lst = input().strip().split()
#print(lst)
ilst = list(map(int,input().strip().split()))
#print(ilst )#
#print(list(ilst))
squared = list(map(lambda x:x**2, ilst))
print(squared)
print("Test1")