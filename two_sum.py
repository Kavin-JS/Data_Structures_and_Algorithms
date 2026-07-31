def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
