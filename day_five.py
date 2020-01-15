'''
用for循环实现1~100之间的偶数求和
'''
sum = 0
for i in range(1,100):
    if i%2 == 0 :
        sum += i

print(sum)
    