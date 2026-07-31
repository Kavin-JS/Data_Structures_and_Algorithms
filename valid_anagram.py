def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] == 0:
            del count[c]
    return len(count) == 0

if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
