with open('input.txt','r') as i:
    list1=eval(i.readline())
    list2=eval(i.readline())
for x in range(len(list1)):
    print('a)',list1[x],'are',list2[x],'ani')
list1.extend(['Andreea','Ioan'])
list2.extend([34,23])
print('b)',list1,'\n',list2)
del(list2[list1.index('Ana')])
list1.remove('Ana')
print('c)',list1,'\n',list2)
print('d)',list1[:3])
print('e)',list1[::-1])
print('f)',list1[2],list2[2],'\n',list1[4],list2[4],'\n',list1[:5],'\n',list2[:5])