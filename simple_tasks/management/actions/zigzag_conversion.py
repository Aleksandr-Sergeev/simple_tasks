sample_string = "PAYPALISHIRING"


class Solution:
    @staticmethod
    def convert(numRows: int=3) -> str:
        # создаем переменные для хранения результата
        dict_of_strings = {num: str() for num in range(numRows)}
        previous_dict_idx = 0
        current_dict_idx = 0
        for letter_idx in range(len(sample_string)):
            dict_of_strings[current_dict_idx] += (sample_string[letter_idx])
            # начало
            if current_dict_idx == 0:
                previous_dict_idx = current_dict_idx
                current_dict_idx += 1
            # проход вниз
            elif current_dict_idx > previous_dict_idx and current_dict_idx < numRows - 1:
                previous_dict_idx = current_dict_idx
                current_dict_idx += 1
            # конец
            elif current_dict_idx == numRows - 1:
                previous_dict_idx = current_dict_idx
                current_dict_idx -= 1
            # проход вверх
            else:
                previous_dict_idx = current_dict_idx
                current_dict_idx -= 1
        return ''.join([val for val in dict_of_strings.values()])



