integer_sample = 1534236469


class Solution:
    @staticmethod
    def reverse() -> int:
        # проверяем что входящее значение - signed 32-bit integer
        global integer_sample
        if integer_sample < (-2 ** 31) or integer_sample > (2 ** 31 - 1):
            return 0
        reversed_int = int(0)
        is_minus, integer_sample = True if integer_sample < 0 else False, abs(integer_sample)
        while integer_sample > 0:
            # добавляем к результату новый разряд
            reversed_int *= 10
            # добавляем в созданный разряд результата остаток от деления на 10
            reversed_int += integer_sample % 10
            # убираем из исходника последний разряд
            integer_sample //= 10
        if reversed_int < (-2 ** 31) or reversed_int > (2 ** 31 - 1):
            return 0
        return reversed_int if not is_minus else reversed_int * -1