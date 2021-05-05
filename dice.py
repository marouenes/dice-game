#!/usr/bin/env python3

from itertools import groupby
from collections import Counter
import re

# command-line input
def user_input():
    print("Enter a single integer N where 1 <= N <= 1000000")
    while 1:
        N = int(input("N: "))
        if N < 1 or N > 1000000:
            print("You entered a wrong value, Please try again!")
        else:
            break

    while 1:        
        chars = input("Enter N characters where each character is a digit from 1 to 6: ")
        seq = list(map(int, list(chars)))
        if len(seq) == N:
            lst = [x for x in seq if x > 6 or x < 1]
            if not lst:
                break
            print("Value should be between 1 and 6 inclusive, Please try again!")
        else:
            print("You entered a wrong number of characters, Please try again!")
    return chars
            
def sixes(input_):
    seq = list(map(int, list(input_)))
    c = Counter(tuple(val) for key, val in groupby(seq))
    return c[(6,6)]

def longest_subsequence(input_):
    splits = input_.split('6')
    lengths = [len(x) for x in splits]
    return max(lengths)

def frequent_lucky(input_):
    lucky = re.split(r"[^56]", input_)
    lucky_length = [len(luck) for luck in lucky if luck]
    if not lucky_length:
        return 0
    frequent = Counter(lucky_length)
    longest = [val for val in frequent if frequent[val] == max(frequent.values())] 
    return max(longest)

if __name__ == '__main__':
    input_chars = user_input()
    print(sixes(input_chars))
    print(longest_subsequence(input_chars))
    print(frequent_lucky(input_chars))


