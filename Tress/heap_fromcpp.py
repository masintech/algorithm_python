#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:46:52 2019

@author: marcus
"""

def Insert(A, n):
    i=n
    temp = A[i]
    while i>1 and temp>A[i//2]:
        A[i] = A[i//2]
        i=i//2
    
    A[i] = temp
    
def Delete(A, n):
#    x = A[n]
    val = A[1]
    A[n-1] = val
    i=1
    j=2*i
    while j<(n-1):
        if A[j+1]>A[j]:
            j+=1
        if A[i]>A[j]:
            A[i], A[j] = A[j], A[i]
            i=j
            j=2*j
        else:
            break
    return val

if __name__ =='__main__':
    H= [0,10,20,30,25,5,40,35];
    for i,ele in enumerate(H):
        if i>=2:
            Insert(H,i)
    for i in range(len(H)-1,1,-1):
        print(Delete(H,i))