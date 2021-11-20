s = input("Write a sentence: ").lower()
s_split = s.split(" ")
count = 0
for i in range(len(s_split)):
    if s_split[i] != '':
        ok = True
        for j in range(i):
            if s_split[i] == s_split[j]:
                ok = False
                break
        if ok:
            count += 1
print(count)
