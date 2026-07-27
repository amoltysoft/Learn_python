# -------------------------:
#---------::lists--------
# [1] List Items Are Inclosed in Square Nrackets
# [2] Lists Are Ordered, To Use Index To Access Item 
# [3] Lists Are Mutable =>you can  Add, end
# [4] List Items Are Not Unque
# [5] List Can Have Different Dat Type
# ------------------------------------------------


# EXAMPLES

my_list = ["one","Two","one",3,4,True]

print (my_list) # will prints all items of list
print (my_list[1]) # prints "Two"
print (my_list[-1]) # prints The last Item in list
print (my_list[-3]) # prints Item  N.O 3 From End

print (my_list[1:4]) # prints Items From Index 1 to Index 3 => ["Two","one",3]
print (my_list[:4]) # prints from Zero Indexing to 3 index => ["one","Two","one",3]
print (my_list[3:]) # prints from 3 Indexing To End list [3,4,True]

print (my_list) # ["one","Two","one",3,4,True]
my_list[1] =2 # edit item [1] to 2
print (my_list) # ["one","2","one",3,4,True]
my_list[2:5] = ["Three",4,"Five"] #edit Items From 2 to 4 
print (my_list) # ["one",2,"Three",4,"Five",True]
my_list[-1] = False # change last Item is False
print (my_list) # ["one","2","Three",4,"Five",False]
my_list[:2] = [1,"tow",3]
print (my_list) # [1,"tow",3,4,"Five",False]
my_list[3:] =["Four",5]
print (my_list) # [1,"tow",3,"Four",5] 
