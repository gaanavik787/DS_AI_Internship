def is_palindrome_slice(text):
    # Convert to string and lowercase to handle numbers and mixed case
    clean_text = str(text).lower()
    # Compare the string with its reverse
    return clean_text == clean_text[::-1]

# Test examples
print(is_palindrome_slice("radar"))  # Returns: True
print(is_palindrome_slice(12321))    # Returns: True
print(is_palindrome_slice("hello"))  # Returns: False
