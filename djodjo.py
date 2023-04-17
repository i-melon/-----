# a = int(input('vvedite kol--vo elementov: '))
# arr = []
# for i in range(0,a,1):
#     b = int(input('vvedite chislo nomer'))
#     arr.append(b)
# print(arr)

# arr = ['one', 'two', 'three']
# arr.append('four')
# arr.clear()
# if len(arr) == 0:
#     print('there is empty')
# else:
#     print('smthng wrong')


a = int(input())
arr = []
cnt = 0
for i in range(0,a,1):
    b = int(input())
    arr.append(b)
for i in arr:
    if i % 2 == 0:
        cnt = cnt+1
print(cnt)






