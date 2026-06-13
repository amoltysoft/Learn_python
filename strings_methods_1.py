#--------------------------------------
#--------strings methods 1--------------
# len(var) => Return var lenth
#var.strip(y) => remove y from right and lift
# y = by defualt whitespace
# var.lstrip(y) => like strip but just from left
# var.rstrip(y) like strip but just from right
# var.capitalize() => change the frist latter form every words is Capital 
# var.title() => change strings to title style
# var.zfill(x) => add zero to fill string to x lenth
# x => lenth with  zero fill  it is start with 2
# var.upper =>uppercase
# var.lower => lowercase
#----------------------------------------------------------

# EXAMPLES

# len()
string1 ="i love python "

print (len(string1))

# var.strip()

print (string1.strip())

# var.strip(y)

str2 ="---------python-------"

print (str2.strip("-")) # y ="-"

# var.rstrip(y)

print (str2.rstrip("-"))

# var.lstrip(y)

print (str2.lstrip("-"))

# var.capitalize()
print (string1.capitalize())

# var.title()

str3 = "i love 3d graphical and 4g technolegy"

print (str3.title())

# var.upper

print (str2)
print (str2.upper())

str4 = "ALwArIThy"
print (str4.lower())

