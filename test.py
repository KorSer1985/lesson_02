test_list = ['a', 'b', 'c']
test_list.append('d')
test_list.insert(2, 'f')
test_list += 'z'
print(test_list)
test_list[2], test_list[3] = test_list[3], test_list[2]
print(test_list)

del test_list[2]
# test_list.remove('c')
print(test_list)
