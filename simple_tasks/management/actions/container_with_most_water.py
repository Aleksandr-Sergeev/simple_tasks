height = [4,3,2,1,4]
height = [1,8,6,2,5,4,8,3,7]
height = [1, 1]

class Solution:
    @staticmethod
    def container_with_most_water() -> str:
        # создаем переменные для хранения результата
        left_pointer = 0
        right_pointer = len(height)-1
        max_volume = 0
        while left_pointer < right_pointer:
            curr_lenght = right_pointer - left_pointer
            current_volume = min(height[left_pointer], height[right_pointer]) * curr_lenght
            max_volume = max(max_volume, current_volume)
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_volume