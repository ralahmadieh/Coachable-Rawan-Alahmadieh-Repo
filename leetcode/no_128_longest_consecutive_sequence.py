def longestConsecutive(self, nums):
    set_of_nums = set(nums)
    length = 0

    for num in nums:
        cur_length = 1
        if num - 1 not in set_of_nums:
            while num + 1 in set_of_nums:
                num = num + 1
                cur_length += 1
        length = max(length, cur_length)

    return length