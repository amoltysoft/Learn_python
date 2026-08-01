#-----------------------------------------------
# ------ Tuple And Method 2 -------------------
# [1] For creat Tuple With One Item  Type Item Then Type Coma
# [2] You Can Concatenate by + 
# [3] Tuple, List, String repeat by *
# [4] Tuple Method 
#	- tuple.count(item) => counts How much item in tuple 
#	- tuple.index(item) => returns index of item in tuple
#	- index method will returns the frist item got it in tuple and ignore others 
# [5] You Can Add Items In Tuple to Varebles 
#------------------------------------------------
# Tuple  with One 

tuple1 = ("it")
print (type(tuple1)) # this is str

# for  tuple 
tuple2 = "this tuple have 1 item",

print (tupleh""qhgqqg2 )
print (type(tuple2))

# Tuple Concatenation 

ta = (1,2,3) # tuple a
tb = (4,5,6) # tuple b
tc = ta + tb # concatenate tuple a and tuple b in tuple c

print (ta) # (1,2,3)
print (tb) # (4,5,6)
print (tc) # (1,2,3,4,5,6)

# remmaber : you can't assign tuple example:
#tc =  ta+(7,8) # error
#but you can add another tuple

td = ta + ("1st","2nd",True) + tb # make tuple d

print (td) # (1,2,3,"1st","2nd",True,4,5,6)

# Tupe , List , String repeat (*)
s = "hi " 		# string
l = ["a","b","c","d "]  # list
t = (1,2,3,4) 	# Tuple

print (s * 4) # prints s 4 times => hi hi hi hi 
print (l * 3) # prints items in  l 3 times =>["a","b","c","d ","a","b","c","d ","a","b","c","d "]
print (t * 5 ) # prints item in t 5 times => (1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4)

# tuple => count()

tuple3 = (1,2,3,1,3,4,5,6,3,4,2,5,6) 
i = 4 # use for get count=> count 4

print (tuple3.count(1)) # count 2
print (f"count {i} is {tuple3.count(i)}") # counts  how many 4

# tuple => index()
t1 = ("1st","2nd","3rd","4th","5th","4th")
print (t1) # ("1st","2nd","3rd","4th","5th")
print (f"index 4th is {t1.index("4th")}") # prints 3 and ignore 5

# tuple to varebles

t2 = "A","B","C","D" # make tuple
char1,char2,char3,char4 = t2 # add t2 items in varebles

print (char1) # "A"
print (char2) # "B"
print (char3) # "C"
print (char4) # "D"

# for ignore item  value and don't  replace name var with _

a,b,_,d =t2 # will ignore c 
print (a)
print (b)
print (d) 
