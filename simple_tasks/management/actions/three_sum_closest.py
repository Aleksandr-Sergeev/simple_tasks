sample_list = [1,1,1,0]  # таргет -100, ответ 3
sample_list = [-1,2,1,-4] # 1, 2
sample_list = [4,0,5,-5,3,3,0,-4,-5] # -2, -2


sample_list = [13,252,-87,-431,-148,387,-290,572,-311,-721,222,673,538,919,483,-128,-518,7,-36,-840,233,-184,-541,522,-162,127,-935,-397,761,903,-217,543,906,-503,-826,-342,599,-726,960,-235,436,-91,-511,-793,-658,-143,-524,-609,-728,-734,273,-19,-10,630,-294,-453,149,-581,-405,984,154,-968,623,-631,384,-825,308,779,-7,617,221,394,151,-282,472,332,-5,-509,611,-116,113,672,-497,-182,307,-592,925,766,-62,237,-8,789,318,-314,-792,-632,-781,375,939,-304,-149,544,-742,663,484,802,616,501,-269,-458,-763,-950,-390,-816,683,-219,381,478,-129,602,-931,128,502,508,-565,-243,-695,-943,-987,-692,346,-13,-225,-740,-441,-112,658,855,-531,542,839,795,-664,404,-844,-164,-709,167,953,-941,-848,211,-75,792,-208,569,-647,-714,-76,-603,-852,-665,-897,-627,123,-177,-35,-519,-241,-711,-74,420,-2,-101,715,708,256,-307,466,-602,-636,990,857,70,590,-4,610,-151,196,-981,385,-689,-617,827,360,-959,-289,620,933,-522,597,-667,-882,524,181,-854,275,-600,453,-942,134]
# -2805, -2805


class Solution:
    @staticmethod
    def three_sum_closest(target=-2805):
        # TODO на последнем сэмпле возвращает неправильный ответ - разобраться
        sample = sample_list.copy()
        sample.sort()
        best_sum = (-(target) + abs(target) + 1)**2
        for index, value in enumerate(sample):
            if index != 0 and value == sample[index - 1]:
                continue
            left_idx = index + 1
            right_idx = len(sample) - 1
            while left_idx < right_idx:
                sum_of_three = value + sample[left_idx] + sample[right_idx]
                if sum_of_three == target:
                    return sum_of_three
                if abs(target - sum_of_three) < abs(target - best_sum):
                    best_sum = sum_of_three
                if best_sum < target:
                    left_idx += 1
                    while sample[left_idx] == sample[left_idx - 1] and index != 0:
                        left_idx += 1
                else:
                    right_idx -= 1
        return best_sum