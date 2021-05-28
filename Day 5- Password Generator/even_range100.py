print("WAY 1")
sum1 = 0
for i in range(0, 101, 2):
    # print(i)
    sum1 += i
print(sum1)

print("-------------------------------------")

sum2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum2+=i
print(sum2)
