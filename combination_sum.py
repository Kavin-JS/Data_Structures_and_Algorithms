def combinationSum(candidates, target):
    res = []
    combo = []

    def backtrack(start, remaining):
        if remaining == 0:
            res.append(combo[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            combo.pop()

    backtrack(0, target)
    return res

if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))
