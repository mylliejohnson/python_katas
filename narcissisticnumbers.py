# A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.
# Ex: 153, where n = 3 (number of digits in 153)
# 13 + 53 + 33 = 153
# Write a method is_narcissistic(i) (in Haskell: isNarcissistic :: Integer -> Bool) which returns whether or not i is a Narcissistic Number.


def is_narcissistic(i):
    # recieve int   
    # int to string
    # string to list
    # loop through list
    # element ^ number of digits
    # append it to total
    # turn list to string 
    # return True if original = total or false 
    
    total = 0
    nums = []
    
    number = str(i)
    
    for num in number:
        n = len(number)
        nums.append(int(num) ** n)
    
    for d in nums:
        total += d
    
    if i == total:
        return True
    else:
        return False