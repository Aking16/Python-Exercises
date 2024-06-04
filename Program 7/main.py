def is_palindrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

print(is_palindrome("گرگ")) 
print(is_palindrome("کتک"))  
print(is_palindrome("radar"))  
print(is_palindrome("hello")) 
