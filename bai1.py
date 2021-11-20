arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newArr = []
newArr1 = []
newArr2 = []

for i in arr:
    newArr.append(i)
    newArr1.append(i)
    newArr2.append(i)

temp = newArr2[:2]
newArr2 = newArr2[2:]
for i in temp:
    newArr2.append(i)

for i in range(len(arr)):
    newArr[i] += 2
    newArr1[i] *= 2

print("Original: ", end="")
for i in arr:
    print(i, end=" ")
print("")
print("Add 2: ", end="")
for i in newArr:
    print(i, end=" ")
print("")
print("Multiple 2: ", end="")
for i in newArr1:
    print(i, end=" ")
print("")
print("Shift 2: ", end="")
for i in newArr2:
    print(i, end=" ")
