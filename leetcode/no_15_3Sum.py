def threeSum(nums):
    nums.sort()
    output_list = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        new_target = - nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == new_target:
                output_list.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif new_target > (nums[left] + nums[right]):
                left += 1
            else:
                right -= 1

    return output_list