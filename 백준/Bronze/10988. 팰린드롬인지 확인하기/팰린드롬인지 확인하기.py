def palindrome(a):
    string_list = list(a)
    reverse_string_list = string_list[::-1]

    if string_list == reverse_string_list:
        print("1")
    else:
        print("0")


string = input()
palindrome(string)