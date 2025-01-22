def trap(height):
    l, r = 0, len(height) - 1
    max_left = height[0]
    max_right = height[-1]
    result = 0

    while l < r:
        if height[l] > height[r]:
            max_right = max(max_right, height[r])
            result += max_right - height[r]
            r -= 1
        else:
            max_left = max(max_left, height[l])
            result += max_left - height[l]
            l += 1

    return result

