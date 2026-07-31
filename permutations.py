def permute(nums):
    res = []

    def backtrack(current, remaining):
        if not remaining:
            res.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return res

if __name__ == "__main__":
    print(permute([1,2,3]))
