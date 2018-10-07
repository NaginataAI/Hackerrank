""" Problem: Lists || Task: 
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer  at position .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

Created on Sun Oct  7 21:18:45 2018
@author: nagiAI
"""

resultList = []
N = int(input())
for i in range (0, N):
    command = input().split()
    
    if command[0] == ("print"):
        print(resultList)
    if command[0] == ("sort"):
        resultList.sort()
    if command[0] == ("pop"):
        resultList.pop()
    if command[0] == ("reverse"):
        resultList.reverse()
    if command[0] == ("remove"):
        resultList.remove(int(command[1]))
    if command[0] == ("append"):
        resultList.append(int(command[1]))
    if command[0] == ("insert"):
        resultList.insert(int(command[1]), int(command[2]))
