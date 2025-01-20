def checkInclusion(s1: str, s2: str):
    hashtable_s1 = [0] * 26
    hashtable_s2 = [0] * 26

    if len(s1) > len(s2):
        return False

    for char in s1:
        hashtable_s1[ord(char) - ord("a")] += 1

    for i in range(len(s1)):
        hashtable_s2[ord(s2[i]) - ord("a")] += 1

    if hashtable_s1 == hashtable_s2:
        return True

    for i in range(len(s1), len(s2)):
        hashtable_s2[ord(s2[i - len(s1)]) - ord("a")] -= 1
        hashtable_s2[ord(s2[i]) - ord("a")] += 1
        if hashtable_s1 == hashtable_s2:
            return True

    return False