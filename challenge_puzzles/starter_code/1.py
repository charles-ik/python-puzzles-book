


def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    new_list =[]
    for element in input_strs:
       if 'a' in element:
           new_list.append(element)
    return new_list
            

  

print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))