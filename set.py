# ----------------------------------
#--------- set --------------------
# [1] set Items Are enclosed in Curly Braces
# [2] set Items Are not ordered and not Indexed
# [3] set not slicing 
# [4] set Has Only Immutable Data Type(Numbers,Strings,Tuples)Lists and Dict Are Not
# [5] set Items is Unique
# -------------------------------------------------



# not ordered and not indexed

set1 = {1,2,"3rd","5th",True,4}
print (set1)

# not indexing example:
#print (set1[1]) # TypeError: 'set' object is not subscriptable

# not slicing example:
#print (set1[0:3]) # TypeError: 'set' object is not subscriptable

# Immutable Data type

set2 = {1,"we",True,(1,2,3)} 

print (set2)

# if you add lists or Dict will get error Examples:

#set3 = {1,2,[1,3,4],"3rd"} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')

#set4 = {2,5,5,{1:"One",2:"Tow"}} # TypeError: cannot use 'Dict' as a set element (unhashable type: 'list')


# set is Unique 

set5 = {1,3,4,5,2,"A","B","C","A","C"}

print (set5)
