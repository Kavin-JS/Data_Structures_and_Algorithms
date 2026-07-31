def lengthOfLongestSubstring(s):
    seen = set()
    l = 0
    best = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        best = max(best, r - l + 1)
    return best

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
