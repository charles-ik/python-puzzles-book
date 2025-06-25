def is_censored_char(input_string: str) -> bool:

    censored_chars = "PYTHON"

    
    input_string.replace(censored_chars,'X')
    
    return input_string


is_censored_char('PsdXdsYdsthonTHON')


def censor_python(input_strs: list[str]) -> list[str]:
    
    '''
    When called, the function should return a new list of strings with the letters
    “P”, “Y”, “T”, “H”, “O”, “N” replaced with “X”, the solution should be case
    insensitive.
    '''
    censored_chars = "PYTHON"

    return 


print(censor_python(["python", "hello", "HELLO"]))
print(censor_python(["abcdefg"]))
print(censor_python([]))
