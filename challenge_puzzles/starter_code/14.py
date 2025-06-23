


def reverse_first_five_positions(input_nums: list[int]) -> list[int]:

    '''
    Function returns new list with first five elements of original list reversed
    Make use of python slicing. No loop are to be used.
    
    '''
    first_half = input_nums[4::-1]
    
    second_half = input_nums[5:]
    return first_half + second_half
    


print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(reverse_first_five_positions([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
print(reverse_first_five_positions([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
