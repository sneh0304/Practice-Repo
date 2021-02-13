def maxCommonality(s):
    res = 0
    for i in range(1, len(s)):
        cur = 0
        x = s[:i]
        y = s[i:]
        print(x)
        print(y)
        for ch in x:
            if ch in y:
                cur += 1
                y = y.replace(ch, '#', 1)
        
        res = max(res, cur)
        print(cur)
    
    return res

s = 'aabbbbaa'
print(maxCommonality(s))