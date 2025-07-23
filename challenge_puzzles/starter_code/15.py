def filter_palindromes(input_strs: list[str]) -> list[str]:
    '''
    Function only returns a new list containing only the strings 
    which are palindrome (same forwards and backward) like racecar
    '''
    output_list = []
    for element in input_strs:
        if element[::-1] == element:
            output_list.append(element)
    
    return output_list


print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))
print(filter_palindromes(["kayak", "deified", "rotator", "repaper", "deed", "a"]))
print(filter_palindromes(["ab", "ba", "cd", "ef", "pt"]))
