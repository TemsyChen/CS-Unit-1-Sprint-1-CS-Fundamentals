'''Imagine a school that children attend for years. 
In each year, there are a certain number of groups started, 
marked with the letters. So if years = 7 and 
groups = 4For the first year, the groups are 
1a, 1b, 1c, 1d, and for the last year, the 
groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school 
by year (as a string), separated with a comma and space 
in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d,
 7a, 7b, 7c, 7d".'''

'''
Iterate over the years, returning a value of year + letter for the range of the groups.
'''

import string
alphabet = list(string.ascii_letters)

def csSchoolYearsAndGroups(years, groups):
    groupsList = []
    for year in range(years):
        for group in range(groups):
            groupsList.append(str(year+1) + alphabet[group])
    separator = ", "
    return separator.join(groupsList)

'''
Create a function that concatenates the number 7 to 
the end of every chord in a list. If a chord already 
ends with a 7, do not add another 7.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["G", "F7", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
'''

'''
Iterate over the array, check if it ends in 7. 
If it does not, add a 7 to the chord. 
Add every chord to a list and return it.
'''

def csMakeItJazzy(chords):
    jazz = []
    for chord in chords:
        if chord.endswith("7"):
            jazz.append(chord)
        else:
            jazz.append(chord + str(7))
    return jazz

    
'''
Given a string of words, return the length 
of the shortest word(s).

Notes:

The input string will never be empty 
and you do not need to validate for different 
data types.
'''

'''
Convert input string into a list of words. 
Iterate over the list checking the length of 
each word and return the shortest word
'''

def csShortestWord(input_str):
    min_length = 100
    words = input_str.split()
    for word in words:
        word_length = len(word)
        if word_length < min_length:
            min_length = word_length
    return min_length

'''
Given an array of integers, return the sum of all 
the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
Notes:

If the input_arr does not contain any positive integers,
 the default sum should be 0.
'''

'''
Iterate over array, save all positive integers 
to a new list. Return the sum of the new list.
'''

def csSumOfPositive(input_arr):
    pos_ints = 0
    for number in input_arr:
        if number >= 1:
            pos_ints += number
    return pos_ints

'''
Given a start integer and an ending integer (both inclusive), 
write a function that returns the count (not the sum) 
of all integers in the range (except integers that 
contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 
(there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
Notes:

The output can contain the digit 5.
The start number will always be less than the end 
number (both numbers can also be negative).
'''
'''
Make a new list of the numbers, excluding any with 5,
 return the length of the list.
'''

def csAnythingButFive(start, end):
    numbers = []
    for i in range(start, end+1):
        if '5' not in str(i):
            numbers.append(i)
    return len(numbers)