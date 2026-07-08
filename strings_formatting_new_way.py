#----------------------------------
#----- string formatting new way ------
# -------syntax
# {} , format(var)
# {:s} => string
#{:d} => integer
# {:f}=>float



#EXAMPLES

name = "alwarithy"
age = 28
height = 1.70


print ("my name is : {}".format(name))
print ("my age is : {}".format(age))
print ("my height is : {}".format(height))
print ("name is {:s} ,age is {:d} , height is {:f}".format(name,age,height))


#you can change index by zero indexing 
#{indx:type}
print ("name is {1:s} ,age is {0:d} , height i is {2:f}".format(age,name,height))

#you can control with floating number by . and num 

print ("name is {1:s} ,age is {0:d} , height i is {2:.2f}".format(age,name,height)) # height get 2 num after dot  =>height is 1.70

# formating mony 

my_mony =50886843

print ("my mony in bank is {:d}".format(my_mony))

#formating 
print("my mony is : {:_d}".format(my_mony)) #put _ between 3 numbers
# error
# print ("{:_}".format("onetowsixten")) # you can't specify _ with string

print ("the reall mony is {:,d} ".format(my_mony))


#formatting in v3.6+

name ="alwarithy"
age =28
sex ="male"

print (f"my name is {name} and my age is {age} and I'm is a {sex}")
