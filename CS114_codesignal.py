'''You are given the prices of a stock, 
in the form of an array of integers, prices. 
Let's say that prices[i] is the price of the 
stock on the ith day (0-based index). 
Assuming that you are allowed to buy and sell 
the stock only once, your task is to find the 
maximum possible profit (the difference 
between the buy and sell prices).

Note: You can assume there are no fees associated 
with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output 
should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on 
day 2 and sell it on day 4. Thus, the maximum profit 
is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be 
buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, 
there's no way to make a profit from selling it. 
Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should 
be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on 
day 0 and sell it on day 1. Thus, the maximum profit 
is prices[1] - prices[0] = 100 - 3 = 97.
'''

def buyAndSellStock(prices):
    if len(prices) < 2:
        return 0
    
    best_buy, best_sell = prices[0:2] 
    potential_buy = best_buy 
    
    for i in range(2, len(prices)):
        value = prices[i]
        if value > best_sell:
            best_sell = value
        if value < potential_buy:
            potential_buy = value
        if value - potential_buy > best_sell - best_buy:
            best_buy = potential_buy
            best_sell = value
    spread = best_sell - best_buy   
    
    if spread < 0: 
        spread = 0
    
    return spread

'''
runtime: O(n)
space: O(1)
'''

    
def buyAndSellStockApproach1(prices):
    profit = 0
    for (i, price) in enumerate(prices):
        for j in range(i, len(prices)):
            diff = prices[j] - price
            if diff > profit:
                profit = diff
    return profit

'''
runtime: O(n^2)
space: O(1)
'''

'''Given a string, your task is to replace each 
of its characters by the next one in the English 
alphabet; i.e. replace a with b, replace b with c,
 etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be 
alphabeticShift(inputString) = "dsbaz".
'''

'''
Plan:
import ascii letters, enumerate them. Replace each character with the next letter in the index, and make a special exception for 'z'.
'''

import string
letters = string.ascii_lowercase

def alphabeticShift(inputString):
    newString = []
    for char in inputString:
        if char == 'z':
            newString.append('a')
        else:
            for i, letter in enumerate(letters):
                if letter == char:
                    newString.append(letters[i+1])
    return "".join(newString)

'''
runtime: O(n)
space: O(n)
'''

'''
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
'''

def validParenthesesSequence(s):
    par = '()'
    while len(s) > 0:
        temp = s
        s = s.replace(par, '')
        if temp == s:
            return False
    return True

'''
runtime: O(n)
space: O(1)
'''