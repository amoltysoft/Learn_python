# -----------------------------------------------
# ---- set Method -------------------------------
# ----------:--------------------------------
# set.clear() => Remove all Elements in set
# set1.union(set2) => Will marge and return  set1 with set2 
# set.add(element) => adds an element to set
# set.remove(elemant) => will remove elemant from set and return none
# if element is not in set will get error
# set.discard(elemant) => like remove  but if not found  will not get error
# set.pop() => return shaffle elemant and remove it from  set
# set1.update(set2) => will update set1 with set2
# you can use list for update set.update(list)
# -------------------------------------------



# clear()
print ("-"*10 + " clear() method")

set1 = {1,2,3,"Dokak",True} 

print (f"set1 after clear is: {set1}")

set1.clear() # remove all element

print (f"set1 befor clear is: {set1}")

print ("="*20)

# =======================================

# union()
print(f"{"-"*10} union()")
set2 = {1,2,3,4,5}

set3 = {"a",7,6,5,8}

print (f"set2 is: {set2}") # prints set2

print (f"set3 is: {set3}") # prints set3

print (f"marge set2,set3 by union() method is: {set2.union(set3)}")
##################################################################

# you can marge 2 sets and more by  union() example: 

set4 = {"b","c","d","ali",True}

print (f"marge set2,set3,set4 is: {set2.union(set3,set4)}")

###############################################

# you can use | for marge also example:

print (f"marge set3 ,set4 by | {set3 | set4}")


print ("="*30)

#########################################################


# add()
print (f"{"-"*10} add()")
set5 = {"1st","2nd","3rd"}

print (f"set5 after add : {set5} ")

set5.add("4th")

print (f"before add 4th element to set5 : {set5}")

##################################################

# remove() 
print (f"{"-"*10} remove()")
set6 = {1,"2nd",3,"4th"}
set6_c = set6.copy()
print (f"set6 = {set6}")
set6.remove("2nd")

print ("will remove 2nd from set6")

print (f"set6 after remove 2nd = {set6}")

#set6.remove(6) #will get  kayerror 

###############################################################

# discard()
print ("="*30)
print (f"{"-"*10} discard()")

print (f"set6_c = {set6_c}") # {'2nd', 1, 3, '4th'}

set6_c.discard(3)

print (f"set6_c after discard(3) = {set6_c}")

print ("="*30)

##########################################################

# pop()

print (f"{"-"*10} pop()")

set7 = {1,2,3,4,"5th",6}

print (f"set7 = {set7}")

print (set7.pop())

print (set7)
print ("="*30)
########################################################

# update()
print (f"{"-"*10} update()")

set8 = {"1st","last","2nd","3rd"}
set9 = {"3rd","4th","5th"}
print (set8)
set8.update(set9) # will update set8 with set9 
print (f"set8 after update with set9 {set8}")

# you can use list for update method example:

print (set9)

set9.update(["6th","7th","1st"])

print  (set9)
