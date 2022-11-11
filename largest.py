l_list = [67,90,89,78,77]
max=l_list[0]
for i in l_list:
    if i>max:
       max=i
print (max)

l1_list = l_list.copy()
print (l1_list)
l1_list.append(90)
print (l1_list)
num=l1_list[0]
for j in l1_list:
    if j==num:
      print(f'the duplicate value is: {j}')
    l1_list.remove(j)
print(f'the new list: {l1_list}')   
