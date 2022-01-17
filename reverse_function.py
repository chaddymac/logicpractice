# create a function that reverses a string

def reverse_function(str_one):
    string_array = []
    # loops starting at the last index
    for i in str_one[::-1]:
        string_array.append(i)
    # use joins to convery arrays to strings
    reversed_string = ''.join(string_array)
    return reversed_string



print(reverse_function("hi dax what are you doing?"))