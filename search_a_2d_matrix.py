def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    l, r = 0, rows * cols - 1
    while l <= r:
        mid = (l + r) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        elif val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

if __name__ == "__main__":
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
