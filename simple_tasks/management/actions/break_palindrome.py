palindrome = 'abcdeedcba'
palindrome = 'abccba'
palindrome = "edcbaabcde"
palindrome = "aaaaaa"


# def break_palindrome(palindrome: str):
#     palindrome_len = len(palindrome)
#     palindrome_half_len = palindrome_len // 2
#     if palindrome_len <= 1:
#         return ""
#     i = 0
#     while i < palindrome_half_len and palindrome[i] == 'a':
#         i += 1
#     if i == palindrome_half_len:
#         return palindrome[:-1] + 'b'
#     else:
#         return palindrome[:i] + 'a' + palindrome[i + 1:]


def break_palindrome(palindrome: str):
    length = len(palindrome)
    if length == 1:
        return ""
    pal = list(palindrome)
    for i in range(length):
        if i == length // 2 and length & 1:
            continue
        if pal[i] != 'a':
            pal[i] = 'a'
            return "".join(pal)
    pal[-1] = 'b'
    return "".join(pal)