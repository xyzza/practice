"""
Boolean function return True, if string is palindrom
or False in another case.
"""


def is_palindrome(string):

    left_index = 0
    right_index = len(string) - 1
    result = False  # not palindrome by default

    while left_index <= right_index:

        if not string[left_index].isalpha():
            left_index += 1
            continue

        if not string[right_index].isalpha():
            right_index -= 1
            continue

        if string[left_index].lower() != string[right_index].lower():
            result = False
            break

        left_index += 1
        right_index -= 1
        result = (
            True  # we are iterating the string containing alphabetic symbols
        )

    return result


# tests:
assert is_palindrome("It's not a palindrome") == False
assert is_palindrome("DoOd")
assert is_palindrome("Don't nod.")
assert is_palindrome("Red rum, sir, is murder")
assert is_palindrome("Eva, can I see bees in a cave?")
assert is_palindrome("") == False
assert is_palindrome("121") == False
