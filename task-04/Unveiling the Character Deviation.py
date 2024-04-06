def incorrect_letters(s):
    reference = "amfoss"
    count = 0
    for i in range(len(reference)):
        if s[i] != reference[i]:
            count += 1
    return count
t = int(input())
for i in range(t):
    s = input().strip()
    incorrect_letters_count = incorrect_letters(s)
    print(incorrect_letters_count )
