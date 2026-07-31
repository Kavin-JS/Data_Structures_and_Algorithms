def maxArea(height):
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        best = max(best, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))
