from collections import Counter

def minWindow(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    missing = len(t)
    l = 0
    bestLen = float("inf")
    bestStart = 0
    for r, c in enumerate(s):
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        while missing == 0:
            if r - l + 1 < bestLen:
                bestLen = r - l + 1
                bestStart = l
            need[s[l]] += 1
            if need[s[l]] > 0:
                missing += 1
            l += 1
    return "" if bestLen == float("inf") else s[bestStart:bestStart + bestLen]

if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))
