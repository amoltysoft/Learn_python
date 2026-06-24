#_-----------------------------------------------++----
#:--------- string formatting old way -------------------------
# place holder 
# %s => formatting string 
# %d => formatting integer 
# %f => formatting floot 

#       syntax 
# "txt %s" % string value 
# "txt %d" % integer value 
# "txt %f" % floot value 
# you can fromat with more then one formatting 
# you can control with string or floot by formatting 
#------------------------------------------------------


# EXAMPLES 

# %S 

name = "Alwarithysoft"
print ("my name is : %s" % name ) # replace %s with name value 

# %d 

age =27 
print (" my age is : %d" % age ) # replace %d with age value 

# %f 
range =12.44
print ("my range is : %f" % range) # replace %f with range value 

# %s %d %f
print ("my name is : %s and my age : %d and my range is : %f" %(name,age,range ))


# %f  control by formatting 

num = 22.05
print ("the number : %f" % num) #defualt formatting  22.050000

print ("the Number is : %.3f" % num) # control to 3 

# %s control by formatting 

str1 = "hello world i am learnning python language"

print ("string is : %s" %str1)
print ("msg is : %.5s everybody" %str1) # slide it from 0 to 5 index 
# note : here the end sliding will in slide 
