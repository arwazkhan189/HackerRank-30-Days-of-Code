#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
no_of_swap=0
for i in range(len(a)-1):
    
    for j in range(len(a)-i-1):
        if (a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            no_of_swap+=1
print("Array is sorted in {} swaps.".format(no_of_swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
