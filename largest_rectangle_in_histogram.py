def largestRectangleArea(heights):
    stack = []
    best = 0
    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            best = max(best, height * (i - idx))
            start = idx
        stack.append((start, h))
    return best

if __name__ == "__main__":
    print(largestRectangleArea([2,1,5,6,2,3]))
