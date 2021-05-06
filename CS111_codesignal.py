'''Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False'''
def csAlphanumericRestriction(input_str):
    if input_str.isdigit():
        return bool(1)
    elif input_str.isalpha():
        return bool(1)
    else:
        return bool(0)

'''Codesignal solution'''
def csAlphanumericRestriction(input_str):
	return input_str.isnumeric() or input_str.isalpha()


'''Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"'''
def csOppositeReverse(txt):
    txt = txt[::-1]
    reversed = []
    for letter in txt:
        if letter.isupper():
            reversed.append(letter.lower())
        elif letter.islower():
            reversed.append(letter.upper())
        else:
            reversed.append(" ")
        # elif letter == " ":
        #     reversed.append(" ")
    joined = "".join(reversed)
    return joined

'''Codesignal solution'''
def csOppositeReverse(txt):
    return txt.swapcase()[::-1]

'''Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9'''
def csSquareAllDigits(n):
    n_string = str(n)
    n_list = list(n_string)
    n_squared = []
    for elem in n_list:
        elem = int(elem)
        elem = elem**2
        n_squared.append(elem)
    n_squared_str = [str(n) for n in n_squared]
    joined_str = "".join(n_squared_str)
    joined_int = int(joined_str)
    return joined_int

'''Codesignal solution'''
def csSquareAllDigits(n):
    return int("".join(str(int(i)**2) for i in str(n)))


'''Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.'''
def csRemoveTheVowels(input_str):
    x = re.sub(r'[aeiouAEIOU]', "", input_str)
    return x

'''Codesignal solution'''
def csRemoveTheVowels(input_str):
    return "".join(c for c in input_str if c.lower() not in "aeiou")