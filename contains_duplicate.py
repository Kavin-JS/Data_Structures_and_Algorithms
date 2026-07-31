def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
