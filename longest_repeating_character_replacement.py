from collections import defaultdict

def characterReplacement(s, k):
    count = defaultdict(int)
    l = 0
    maxFreq = 0
    best = 0
    for r in range(len(s)):
        count[s[r]] += 1
        maxFreq = max(maxFreq, count[s[r]])
        while (r - l + 1) - maxFreq > k:
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best

if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))
