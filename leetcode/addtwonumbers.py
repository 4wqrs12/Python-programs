l1 = [2,4,3]
l2 = [5,6,4]

num1 = ""
for i in l1[::-1]:
    num1 += str(i)

num2 = ""
for j in l2[::-1]:
    num2 += str(j)

num_sum = int(num1)+int(num2)
str_sum = str(num_sum)
res = []
for i in str(str_sum[::-1]):
    res.append(int(i))

print(res)

