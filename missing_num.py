p = 101
q = p
l = []
l1 = []
for i in range(1,p):
    l.append(i)
for y in range(1,q):
    l1.append(y)
delete = int(input('Enter a number to delete from the list: ' ))
l1[delete - 1] = 0
for i in range(len(l)):
    if l[i] != l1[i]:
        print(i+1)
        break