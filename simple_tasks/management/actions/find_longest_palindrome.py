sample_string = "babaddab"


class Solution:
    @staticmethod
    def find_longest_palindrome() -> str:
        max_lenght = 0
        result = str()
        for i in range(len(sample_string)):
            # нечетная длина
            left, right = i, i
            while left >= 0 and right < len(sample_string) and sample_string[left] == sample_string[right]:
                if (right - left + 1) > max_lenght:
                    max_lenght = right - left + 1
                    result = sample_string[left:right + 1]
                left -= 1
                right += 1
            # четная длина
            left, right = i, i+1
            while left >= 0 and right < len(sample_string) and sample_string[left] == sample_string[right]:
                if (right - left + 1) > max_lenght:
                    max_lenght = right - left + 1
                    result = sample_string[left:right + 1]
                left -= 1
                right += 1
        return result

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s   # If the string itself is a palindrome
        size = len(s)               # Total chars in text

        # Always match 1st char since one char is technically a palindrome
        j, k = 1, 0                 # Length of longest substring match; index position of longest match
        for i in range(1, size):    # Loop through each char (skip first char since it's evaluated in the loop)
            si = i - j              # Start position of substring index
            a = s[si - 1:i + 1]     # Substring of cur position +/- 2 chars
            b = s[si:i + 1]         # Substring of cur position +/- 1 char

            # Evaluate 2+ chars away from current position
            if si > 0 and a == a[::-1]:
                j += 2              # Increment by 2 to include previous char
                k = si - 1          # Set index position of longest char match
                continue

            # Check next char vs current substring
            if b == b[::-1]:
                j += 1              # Increment longest substring length by 1
                k = si

        return s[k:k + j]



