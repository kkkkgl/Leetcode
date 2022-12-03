# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:18:45 2022

@author: kn.dang
"""
''' 
总共有n级台阶
in total there are n steps 
we clime ones or two steps each time 
how many ways to go from the ground to the first step 

'''
from math import factorial as fact


def steps(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    if n < 3:
        return dp[n]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def recur_steps(n):
    if n <= 2:
        return n
    else:
        return recur_steps(n-1) + recur_steps(n-2)
    
def math_steps(n):
    ans = 0
    pairs = []
    for i in range(n+1):
        if (n - i) % 2 == 0:
            pairs.append((i, int((n-i)/2)))
    for ones, twos in pairs:
        ans += fact(ones+twos)/(fact(ones)*fact(twos))
    return ans

print(recur_steps(4))