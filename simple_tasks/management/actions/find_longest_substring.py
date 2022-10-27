sample_string = 'abccba'
sample_string = 'edcbaabcde'
sample_string = "aaaaaa"
sample_string = 'abcdeedcba'
sample_string = 'pwwkew'
sample_string = ' '
sample_string = 'dvdf'
sample_string = 'cdd'
sample_string = 'cancanviajm'


class Solution:
    @staticmethod
    def find_longest_substring() -> int:
        charBucket = set()
        left = 0
        result = 0

        for right in range(len(sample_string)):
            while sample_string[right] in charBucket:
                charBucket.remove(sample_string[left])
                left += 1
            charBucket.add(sample_string[right])
            result = max(result, right - left + 1)
        return result

    @staticmethod
    def find_longest_substring_my() -> int:
        max_len = 0
        curr_str = []
        curr_len = 0
        local_string = sample_string
        curr_pos = 0
        while True:
            try:
                curr_element = local_string[curr_pos]
            except IndexError:
                return max(max_len, len(local_string))
            if curr_element not in curr_str:
                curr_str.append(curr_element)
                curr_pos += 1
            elif curr_element in curr_str:
                curr_len = len(curr_str)
                local_string = local_string[local_string.index(curr_element) + 1::]
                curr_str = []
                curr_pos = 0
            if curr_len > max_len:
                max_len = curr_len

    @staticmethod
    def find_longest_substring_backup() -> int:
        max_len = 0
        curr_str = []
        for pos, item in enumerate(sample_string):
            if item not in curr_str:
                curr_str.append(item)
            else:
                curr_str = list({sample_string[pos - 1], item})
            if len(curr_str) > max_len:
                max_len = len(curr_str)
        return max_len