# удаление символа
initial = 'abced'
target = 'abcd'
# добавление символа
initial = 'abcd'
target = 'abced'
# замена символа
initial = 'abced'
target = 'abcfd'



class Solution:
    @staticmethod
    def get_target_str() -> bool:
        initial_len = len(initial)
        target_len = len(target)
        if initial_len >= target_len + 2:
            return False
        if initial == target:
            return True
        operations_count = 0
        current_init_idx = 0
        current_target_idx = 0
        result = str()
        while operations_count <= 1 and current_target_idx+1 <= target_len and current_init_idx+1 <= initial_len:
            if initial[current_init_idx] == target[current_target_idx]:
                result += target[current_target_idx]
                current_target_idx += 1
                current_init_idx += 1
            # кейс под удаление символа
            elif initial_len > target_len:
                result += target[current_target_idx]
                current_init_idx += 2
                current_target_idx += 1
                operations_count += 1
            # кейс под добавление символа
            elif initial_len < target_len:
                result += target[current_target_idx]
                current_target_idx += 1
                operations_count += 1
            # кейс под замену символа
            else:
                result += target[current_target_idx]
                current_target_idx += 1
                current_init_idx += 1
                operations_count += 1
        return result == target


    # @staticmethod
    # def get_target_str() -> bool:
    #     initial_len = len(initial)
    #     target_len = len(target)
    #     if initial_len >= target_len + 2:
    #         return False
    #     if initial == target:
    #         return True
    #     operations_count = 0
    #     current_init_idx = 0
    #     current_target_idx = 0
    #     result = str()
    #     while operations_count <= 1 and current_init_idx <= initial_len-1:
    #         # символы совпадают
    #         if initial[current_init_idx] == target[current_target_idx]:
    #             result += target[current_target_idx]
    #             current_init_idx += 1
    #             current_target_idx += 1
    #         # удаление символа
    #         elif initial[current_init_idx + 1] == target[current_target_idx]:
    #             result += target[current_target_idx]
    #             current_init_idx += 2
    #             current_target_idx += 1
    #             operations_count += 1
    #         # добавление символа
    #         elif initial[current_init_idx] == target[current_target_idx + 1]:
    #             result += target[current_target_idx]
    #             current_init_idx += 1
    #             current_target_idx += 1
    #             operations_count += 1
    #         # замена символа
    #         else:
    #             result += target[current_target_idx]
    #             current_init_idx += 1
    #             current_target_idx += 1
    #             operations_count += 1
    #     return True if result == target else False





