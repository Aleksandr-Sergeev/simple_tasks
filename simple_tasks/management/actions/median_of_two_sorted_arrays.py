nums1 = [0, 1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10, 11, 12, 13, 14]


# TODO разобраться с логикой на свежую голову))
class Solution:
    @staticmethod
    def median_of_two_sorted_arrays() -> float:
        # создаем переменные для хранения результата
        listA, listB = nums1, nums2
        total = len(listA) + len(listB)
        half = total // 2

        if len(listA) > len(listB):
            listA, listB = listB, listA

        left, right = 0, len(listA) - 1

        while True:
            i = (left + right) // 2  # ?указатель на середину листа А
            j = half - i - 2  # ?указатель на позицию листа 2 - элементы левее могут входить в левую часть объединенного листа

            Aleft = listA[i] if i >= 0 else float('-infinity')
            Aright = listA[i+1] if i+1 < len(listA) else float('infinity')
            Bleft = listB[j] if j >= 0 else float('-infinity')
            Bright = listB[j+1] if j+1 < len(listB) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                # нечетная длина общего листа
                if total % 2:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1