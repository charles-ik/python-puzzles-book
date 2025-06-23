def has_vowel(input_str: str) -> bool:
    '''
    Takes an input string and returns True if it contains a vowel 
    '''

    for vowel in 'aeiou': 
        if vowel in input_str: 
            return True
        
    return False
        

    

def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
    '''
    Function takes one parameter
    When called function returns a new list with all strings that have at least one vowel
    '''
    new_list = []

    for element in input_strs:
        if has_vowel(element) == True:
            new_list.append(element)
        else:
            continue
    return new_list

def filter_with_bool(input_strs):
    new_list =[]

    for word in input_strs:
        if bool(set(word) & set('aeiou')): # & operator when used with sets returns True if sets overlap
            new_list.append(word)
    
    return new_list

def filter_with_any(input_strs: list[str]) -> list[str]:
    
    return([string for string in input_strs if has_vowel(string)])

def filter_with_any_2(input_strs: list[str]) -> list[str]:
    ''' Using generator expression and any function
    '''
    return([string for string in input_strs if any(vowel in string for  vowel in 'aeiou')])



print("Let's see what the generator expression does:")
string = "apple"
gen_expr = (v in string for v in 'aeiou')
print(type(gen_expr))  # <class 'generator'>
print(list(gen_expr))  # [True, True, False, False, False]

# any() consumes this generator and returns True if ANY value is True
print(any(v in "apple" for v in 'aeiou'))  # True
print(any(v in "xyz" for v in 'aeiou'))    # False

print('\nOrginial functions')

print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))
print(filter_strings_with_vowels([]))
print(filter_strings_with_vowels(["q", "w", "e", "r", "t", "y"]))
print(filter_strings_with_vowels(["ae", "io", "aeiou"]))

print("\nFilter with bool function")
print(filter_with_bool(["apple", "banana", "zyxvb"]))
print(filter_with_bool([]))
print(filter_with_bool(["q", "w", "e", "r", "t", "y"]))
print(filter_with_bool(["ae", "io", "aeiou"]))

print("\n First filter with any function")
print(filter_with_any(["apple", "banana", "zyxvb"]))
print(filter_with_any([]))
print(filter_with_any(["q", "w", "e", "r", "t", "y"]))
print(filter_with_any(["ae", "io", "aeiou"]))

print("\n Second filter with any function")
print(filter_with_any_2(["apple", "banana", "zyxvb"]))
print(filter_with_any_2([]))
print(filter_with_any_2(["q", "w", "e", "r", "t", "y"]))
print(filter_with_any_2(["ae", "io", "aeiou"]))


# def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
#     '''
#     Function takes one parameter
#     When called function returns a new list with all strings that have at least one vowel
#     '''
#     vowels = ['a','e','i','o','u']
#     new_list = [] # create the empty list to be retuned at the end when function is called
#     counter = 0 
#     while counter <= (len(vowels) - 1):
#         char = vowels[counter]
        
#         for element in input_strs:
#             if char in element:
#                 new_list.append(element)
#             else:
#                 continue
#         counter += 1
    
#     return new_list