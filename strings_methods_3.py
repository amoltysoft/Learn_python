# -----------------------------------------------------
# ----strings methods 3 -----------------------------
# var.index(sub,start,end) =>  returns sub's index if sub not found will returns error
# var.find(sub,start,end)=>it's like index method but if sub not found returns -1
# var.just => 
#
#
#------------------------------------------------------ 

# === EXAMPLES 👇

# var.index() casesensitive
str1 = "Hi Everyone I'm Learning Python"
indexpy = str1.index("Python") # returns index 25

print (indexpy)

indexpy = str1.index("I'm",0,31) # returns index 8
print (indexpy) 
#indexpy = str1.index("Python",10,20) # Error
#print (indexpy)

# var.find() casesensitive

str2="hi everybody"

print (str2.find("body"))
print (str2.find("every",3,12)) #return 3
print (str2.find("hi",1,11)) #return -1



