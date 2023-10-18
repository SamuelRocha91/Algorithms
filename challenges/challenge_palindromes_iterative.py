def is_palindrome_iterative(word):
    if not word:
        return False
    inverse = ''
    for i in range(len(word) - 1, -1, -1):
        inverse += word[i]
    return word == inverse
