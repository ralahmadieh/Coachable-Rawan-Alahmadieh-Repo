def maxArea(height):
    l, r = 0, len(height) - 1
    area = 0

    while l < r:
        current_area = min(height[l], height[r]) * (r-l)
        area = max(area, current_area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return area