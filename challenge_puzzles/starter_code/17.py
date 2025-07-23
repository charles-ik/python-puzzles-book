from collections import defaultdict

#String is happy if the consecutive characters are different




# this works for two consecutive characters 
def check_if_string_is_happy(input_str: str) -> bool:

    string_dic = defaultdict(str)
    
    for char in input_str: 
        if char == string_dic['previous string']:
            is_happy = False
            break
        else:
            is_happy = True
        string_dic['previous string'] = char

    return is_happy


def check_if_string_is_happy(input_str: str) -> bool:
    for i in range(len(input_str) - 2): #makes sure exactly three characters are checked at the end of string
        three_chars = input_str[i:i+3] #note: slicing doesn't error if we go over 3 characters. python returns the last character instead. 
        if len(set(three_chars)) != 3:
            return False
    return True

## another solution
def check_if_string_is_happy(input_str: str) -> bool:
    return not any(
        a == b or a==c or b == c 
        for a,b,c in zip(input_str, input_str[1:],input_str[2:]) 
    )



print(check_if_string_is_happy("abcdefg"))
print(check_if_string_is_happy("abcabcabcabc"))
print(check_if_string_is_happy("hello"))
