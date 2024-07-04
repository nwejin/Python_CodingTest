a = ['a1', 'b2', 'c3']

for i in range(len(a)):
    print('방법 1',i, a[i])

j = 0
for v in a:
    j += 1
    print('방법 2', j, v)



for p, q in enumerate(a):
    print(p, q)