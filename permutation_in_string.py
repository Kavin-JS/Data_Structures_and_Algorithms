from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    need = Counter(s1)
    window = Counter(s2[:len(s1)])
    if window == need:
        return True
    for i in range(len(s1), len(s2)):
        window[s2[i]] += 1
        left = s2[i - len(s1)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == need:
            return True
    return False

if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))
