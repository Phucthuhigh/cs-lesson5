# n = int(input("Nhap so luong mon an hoac bi dam daddy phat: "))
# a = []

# for i in range(n):
#     a.append(input(f"mon an {i + 1}: "))

# for i in a:
#     print(i)

# food = input("Xoa so mon an: ")
# try:
#     a.remove(food)
# except:
#     print("khong co mon nay trong list cua ban")
# for i in a:
#     print(i)

# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# for i in a:
#     print(i, end=" ")
# s = 0
# for i in a:
#     s += i
# max = a[0]
# for i in a:
#     if max <= i:
#         max = i
# print(f"\nsum = {s}\nmax = {max}")
# n = int(input())
# a = []

# for i in range(n):
#     a.append(int(input()))

# for i in range(n-1):
#     for j in range(i+1, n):
#         if a[i] >= a[j]:
#             tmp = a[i]
#             a[i] = a[j]
#             a[j] = tmp

# for i in a:
#     print(i, end=" ")

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# newArr = []
# newArr1 = []
# newArr2 = []

# for i in arr:
#     newArr.append(i)
#     newArr1.append(i)
#     newArr2.append(i)

# temp = newArr2[:2]
# newArr2 = newArr2[2:]
# for i in temp:
#     newArr2.append(i)

# for i in range(len(arr)):
#     newArr[i] += 2
#     newArr1[i] *= 2

# print("Original: ", end="")
# for i in arr:
#     print(i, end=" ")
# print("")
# print("Add 2: ", end="")
# for i in newArr:
#     print(i, end=" ")
# print("")
# print("Multiple 2: ", end="")
# for i in newArr1:
#     print(i, end=" ")
# print("")
# print("Shift 2: ", end="")
# for i in newArr2:
#     print(i, end=" ")

# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
#        'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
# s = ""
# for i in range(len(arr)):
#     s += arr[len(arr)-i-1]
# print(s)

# f = [1, 1]
# n = int(input())
# for i in range(2, n):
#     f.append(f[i-1] + f[i-2])

# for i in range(n):
#     print(f[i], end=" ")

# n = int(input("Number of items: "))
# print("")
# a = []
# for i in range(n):
#     name_food = input(f"Item {i + 1}: ")
#     price_food = float(input(f"Price of item {i + 1}: "))
#     item = {
#         "name": name_food,
#         "price": price_food
#     }
#     a.append(item)
#     print("")

# total_price = 0
# for i in range(n):
#     total_price += a[i]["price"]

# average_price = round(total_price / n, 2)

# filter_list = []

# for i in range(n):
#     if a[i]["price"] > average_price:
#         filter_list.append(a[i])

# print("")

# print(f"Average price: {average_price}")
# print("Item(s) above average price: ", end="")
# for i in filter_list:
#     print(f"('{i['name']}, {i['price']}')", end=" ")

# s = input("Write a sentence: ").lower()
# s_split = s.split(" ")
# count = 0
# for i in range(len(s_split)):
#     if s_split[i] != '':
#         ok = True
#         for j in range(i):
#             if s_split[i] == s_split[j]:
#                 ok = False
#                 break
#         if ok:
#             count += 1
# print(count)
