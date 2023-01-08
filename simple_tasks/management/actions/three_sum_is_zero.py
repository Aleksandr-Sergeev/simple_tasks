sample = [-1, -4, 0, 1, 2, 1, -1, -1, -3, 4]


class Solution:
    @staticmethod
    def three_sum_is_zero():
        result = []
        sample.sort()
        for index, value in enumerate(sample):
            if index > 0 and value == sample[index-1]:
                continue
            left_idx = index + 1
            right_idx = len(sample) - 1
            while left_idx < right_idx:
                sum_of_three = value + sample[left_idx] + sample[right_idx]
                if sum_of_three == 0:
                    result.append([value, sample[left_idx], sample[right_idx]])
                    left_idx += 1
                    while left_idx < len(sample) - 1 and sample[left_idx] == sample[left_idx - 1]:
                        left_idx += 1
                elif sum_of_three > 0:
                    right_idx -= 1
                else:
                    left_idx += 1
        return result

    @staticmethod
    def three_sum_is_zero_another():
        nums = sample
        res = set()
        nums.sort()
        hashmap = {n: i for i, n in enumerate(nums)}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twosum = -nums[i]
            for j in range(i + 1, len(nums)):
                target = twosum - nums[j]
                if target in hashmap and hashmap[target] > j:
                    res.add((nums[i], nums[j], target))
        return list(res)