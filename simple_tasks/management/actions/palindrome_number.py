number = 121


class Solution:
    @staticmethod
    def is_palindrome() -> bool:
        global number
        # первичные проверки
        if number < 0 or number > (2 ** 31):
            return False
        # создаем переменные для хранения результата
        local_number = number
        reversed_number = 0
        while local_number > 0:
            reversed_number *= 10
            reversed_number += local_number % 10
            local_number //= 10
        return True if reversed_number == number else False