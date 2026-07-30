#------------------------------------
# ------- lists method 2 -------------
# list.clear() => clear all item in list
# list.copy() => return a shadow from list
# list.count(item/s) => count item/s in the list 
# list.index(object) => get and return index of object
# if object is not in list get error
# list.insert(indx,object) => insert object in list 
# after indx index
#  list.pop(indx) => remove and return item of indx
#--------------------------------------


#EXAMPLE

# clear()

list1 = ["a",3,5,7,True]

print (list1) # ["a",3,5,7,True]

list1.clear() # clear list1 
print (list1) # []

# copy()

list2 = [1,2,3,4]
list2_copy = list2.copy() # get a copy from list2
print (list2) # [1,2,3,4]
print (list2_copy) # [1,2,3,4]
list2.append(5) #add 5 

print (list2) # [1,2,3,4,5]
print (list2_copy) # [1,2,3,4]
list2.remove(2) # remove 2 
print (list2) # [1,3,4,5]
print (list2_copy) # [1,2,3,4]

# count(item/s)

list3 = [1,2,4,3,2,2,1,3,5,6]

print (list3) #[1,2,4,3,2,2,1,3,5,6]
i = 2
print (f"count {i} in list3 is {list3.count(i)}")
print (list3.count(8))

# index(object)

list4 = ["a","b","c","d"]
print (list4) # ["a","b","c","d"]
i = "c"
print (f"index of {i} is {list4.index(i)}") # index c is 2

# insert()
list4.insert(0,"9") # insert "9" after index 0
print (list4) # ["9","a","b","c","d"]
list4.insert(2,"bb") # add "bb" after index 2
print (list4) # ["9","a","bb","b","c","d"]
# pop()

list5 = ["ahmed","mohamed","ali"]
print (list5) # ["ahmed","mohamed","ali"]
print (list5.pop(1)) # mohamed

print (list5) # ["ahmed","ali"]

