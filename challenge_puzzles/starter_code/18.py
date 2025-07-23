#What a recursive function 
# A function that calls itself

#example: 

'''
def factorial(n):
    if n == 1:
        return 1  # base case
    return n * factorial(n - 1)  # recursive call
'''



def get_number_of_digits(input_num: int) -> int:
    '''
    When called, the function should return the number of digits in the input_num.
        Caveats:
        The function should be recursive
        The function should not convert the integer to a string
    
    '''
    
    count += 1 
    return count


print(get_number_of_digits(1234))
print(get_number_of_digits(0))
print(get_number_of_digits(123456789))
