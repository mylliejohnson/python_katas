# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):

# notes:  
# 16 is our number
# should return 60
# number of multiples of 3 or 5; if number repeats, show once
# 3s - 3, 6, 9, 12, 15
# 5s - 5, 10, 15
#   = 75 ---> 60!
#     ex_sum = [3, 6, 9, 5]
#     skip = 0
#     ex_total = 0
#     for i in ex_sum:
#             ex_total += i  
#     print(ex_total) # 75

    sum = 0
    factors = []
    
    for num in range(1,number+1):
        if num % 3 == 0 or num % 5 == 0:
            factors.append(num)
        if number < 0:
            return 0
            
    for n in factors:
        if n < number:
            sum += n

    return sum