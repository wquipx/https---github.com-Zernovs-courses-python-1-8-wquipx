'''
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий 
элементы списка, а не их индексы!
'''
arr = list(map(int, input().split()))

for i in arr:
    if not i % 2:
        print(i, end = " ")