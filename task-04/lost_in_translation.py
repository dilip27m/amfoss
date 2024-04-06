def hello(s):
    requiredletters = ['h', 'e', 'l', 'l', 'o']
    index = 0
    for char in s:
        if char == requiredletters[index]:
            index += 1
            if index == len(requiredletters):
                return True
    return False
s= input().strip()
if hello(s):
    print("YES")
else:
    print("NO")
