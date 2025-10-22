def reverse_string(string):
    return string[::-1]




def is_palindrome(string):
    if string == reverse_string(string):
        return ("its a palindrome")
    else: return ("its not a palindrome")
