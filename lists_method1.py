# ----------::::-----------------------------
# --------------- lists method 1 ------------
# list.append(item) => add one item or more to list
# if item is unathor  list append  method  add it like a list 
# list.extend(item) => like append but if item  is list 
# will add items in child list
# list.remove(val) => removes the frist val get it in the list
# list.sort(reverse=False/True) = > sort items by a-z or 1-9 
# reverse by defult is False 
#---------------------------


# EXAMPLES

# append()

list1 = ["first","second","third","fourth"]
print (list1) # ["first","second","third","fourth"]


list1.append("5th")
print (list1) # ["first","second","third","fourth","5th"]

list1.append(2026)
print (list1) # ["first","second","third","fourth","5th",2026]

list1.append(True)
print (list1) # ["first","second","third","fourth","5th",2026,True]

list1.append(["1st","2nd","3rd","4th"])
print (list1) # ["first","second","third","fourth","5th",2026,["1st","2nd","3rd","4th"]]


# for access any item type index it 
print (list1[5]) # 2026

print (list1[-1]) # ["1st","2nd","3rd","4th"]

# for  access item in child list type index child list and  index item 
list1[-1].append("last")
print (list1) #["first","second","third","fourth","5th",2026,["1st","2nd","3rd","4th","last"]]

print (list1[-1]) # ["1st","2nd","3rd","4th","last"]
print (list1[-1][1]) # 2nd
print (list1[-1][-1]) # last

# extend 

list2 = [1,2,3,4]

print (list2) # [1,2,3,4]

list3 = ["one","Tow","Three","Four"]

list2.extend(list3) # will add list3 items to list2 as items

print (list2) # [1,2,3,4,"one","Tow","Three","Four"]

list1.extend(list2) # add list2 items to list 1 as items

print (list1) # ["first","second","third","fourth","5th",2026,["1st","2nd","3rd","4th","last"],1,2,3,4,"one","Tow","Three","Four"]

# remove

list4 = [1,2,3,2,4,2,5,2]
print (list4) # [1,2,3,2,4,2,5,2]
list4.remove(2)
print (list4) # [1,3,2,4,2,5,2]

# sort 

list5 = [1,-5,-12,33,45,-105,22]
print (list5) # [1,-5,-12,33,45,-105,22]

list5.sort()
print (list5) # [-105,-12,-5,1,22,33,45]
list6 = ["d","b","a","c"]
print (list6)
list6.sort()
print (list6) # [a,b,c,d]

list7 = [1,5,3,"a",7,"b","d","c"]
print (list7)
# list7.sort() # error becouse can't sort int with str
list8 =["1st","4th","3rd","2nd"]
print (list8)
list8.sort()
print (list8)

# sort(reverse=True) => will reverses sorting z-a or 9-0

list9 = [1,-5,-12,33,45,-105,22]
print (list9) # [1,-5,-12,33,45,-105,22]
list9.sort(reverse=True)
print (list9) # [45,33,22,1,-5,-12,-105]


# reverse => reverses items in list not sorting
list10 = [3,4,2,1,"a","c","b"]
print (list10) # [3,4,2,1,"a","c","b"]

list10.reverse()
print (list10) # ["b","c","a",1,2,4,3]


# end 
