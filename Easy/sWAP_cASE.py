""" Problem: sWAP cASE || Task: 
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Created on Wed Oct 10 10:50:38 2018
@author: nagiAI
"""
def swap_case(s):
    result = ""
    for i in s:
        if (ord(i) >= 97) and (ord(i) <= 122):
            result += i.upper()
        elif (ord(i) >= 65) and (ord(i) <= 90):
            result += i.lower()
        else:
            result += i
    return result

#print(swap_case("Pythonist 2 "))
