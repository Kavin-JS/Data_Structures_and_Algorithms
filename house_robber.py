def rob(nums):
    prev, curr = 0, 0
    for n in nums:
        prev, curr = curr, max(curr, prev + n)
    return curr

if __name__ == "__main__":
    print(rob([1,2,3,1]))
    print(rob([2,7,9,3,1]))
