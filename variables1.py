#-----------------------
#---------- variables 1 -------
# syntax variables 👉 name =  value
#
# namevConvention and Rules
# 1) you can start with (a-z A-Z) or underscore
# 2) you can not start with number or special charcter
# 3) you can include (0-9) or underscore
# 4) you can not include special characters
# 5) name is not Name [case sensitive]
#
# best practes
# 1) singel word 
# 2) camelCase =>towWords or more
# 3) snake_case tow_words_or_more
# ---------------------------------------

#--- EXAMPLES

#--syntex
#name = value
a = 20
print (a)

#----rules
# 1
_b =10
print (_b)
b = 11
print (b)
B =12
print (B)

#2 
#1a = 1 #error
#-c = 2 # error

#3
a2z ="a b c d e f g h i j k l m n o b q r s t u v w x y z "
print (a2z)

# 4 
# a-c ="error" #error
name = "this is not Name var"
print (name)

Name = "this not name var "
print (Name)

#----best practes

# 1 
word ="singal words"
print (word)
# 2
camalCase ="thisCamalCase"
print (camalCase)

# 3
snake_case ="snake_case_way"
print(snake_case)
