def is_censored_char(input_string: str) -> list[str]:


    censored_chars = "PYTHON"

    new_list =[]
    for letter in input_string:
        if letter.upper() in censored_chars:
            new_list.append('X')
            # is_censored = True
        else:
            new_list.append(letter)
            
    
    
    return new_list


# print(is_censored_char('PsdXdsYdsthonTHON'))


def censor_python(input_strs: list[str]) -> list[str]:
    
    '''
    When called, the function should return a new list of strings with the letters
    “P”, “Y”, “T”, “H”, “O”, “N” replaced with “X”, the solution should be case
    insensitive.
    '''

    new_list = []
    for word in input_strs: 
        lst1 = is_censored_char(word)
        new_word = ''.join(lst1)
        new_list.append(new_word)

    return new_list



print(censor_python(["python", "hello", "HELLO"]))
print(censor_python(["abcdefg"]))
print(censor_python([]))




# tip for review 
# you can concatonate strings so something like 

'''
def censor_python(input_strs: list[str]) -> list[str]:
    # What letters need to be replaced?
    censored_letters = "PYTHON"  # Work in uppercase for easier checking
    
    # Process each string in the list
    result = []
    for string in input_strs:
        # For each string, build a new censored version
        new_string = ""
        for char in string:
            # Check each character...
            if char.upper() in censored_letters:
                new_string += "X"  # What should go here?
            else:
                new_string += char  # What should go here?
        result.append(new_string)
    
    return result
'''
        
# other great solutions 

'''
def censor_python(input_strs: list[str]) -> list[str]:
    censored = "PYTHON"
    return [''.join('X' if c.upper() in censored else c for c in s) 
            for s in input_strs]


def censor_python(input_strs: list[str]) -> list[str]:
    # Create translation table for both upper and lowercase
    trans_table = str.maketrans('PYTHONpython', 'X' * 12)
    return [s.translate(trans_table) for s in input_strs]


import re

def censor_python(input_strs: list[str]) -> list[str]:
    # [PpYyTtHhOoNn] matches any of these characters
    pattern = re.compile(r'[PYTHON]', re.IGNORECASE)
    return [pattern.sub('X', s) for s in input_strs]


def censor_python(input_strs: list[str]) -> list[str]:
    censored = set('PYTHON')  # Set for O(1) lookup
    
    def censor_char(c):
        return 'X' if c.upper() in censored else c
    
    def censor_string(s):
        return ''.join(map(censor_char, s))
    
    return list(map(censor_string, input_strs))


def censor_python(input_strs: list[str]) -> list[str]:
    censored = frozenset('PYTHON')  # Immutable set
    
    def censor_string(s):
        return ''.join('X' if c.upper() in censored else c for c in s)
    
    # Generator expression - processes one at a time
    return list(censor_string(s) for s in input_strs)

'''
    


