def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res

if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))
