def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    max_index = len(word) - 1
    inverse_word = is_palindrome(word, 0, max_index)
    if inverse_word == word:
        return True
    else:
        return False


def is_palindrome(word, low_index, high_index):
    if not word:
        return False
    if len(word) == 1:
        return word
    num = len(word) - 1
    inverse = is_palindrome(word[1:], 0, num) + word[0]
    return inverse


print(is_palindrome_recursive("lula", 0, 3))
