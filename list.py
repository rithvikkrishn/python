test_list1 = [1, 3, 4, 6, 8] 
test_list2 = [4, 5, 6, 2, 10] 
print ("Original list 1 : " + str(test_list1)) 
print ("Original list 2 : " + str(test_list2))  
list = [] 
for i in range(0, len(test_list1)): 
    list.append(test_list1[i] + test_list2[i]) 
print ("the list is : " + str(list)) 
