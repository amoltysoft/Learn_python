#-------------------------------------------
# ----------Strings 2 Indexing And Slicing -----------------------------------
# All Data In Python Is Objects
# Object Conaint Elements
# Every Element Has Its Own Index
# Python Use Zero Based Indexing (Index Start From Zero)
# Use Square Brackets to Access Element
# Enable Accessing Parts of Strings, Tuples or Lists
#----------------–—————

#indexing ( Access single Element )

string1 = "go to your school"

print (string1[0]) # index 0 => g

print (string1[11]) #index 11 => s 

print (string1[-1]) # index -1 => Frist Character From End Guess it

print (string1[-5]) # index -5 => Count From End

# slicing (Access Multiple Sequences Items )

# 1[start : End]
print (string1[0:3]) # slicing => go

# End Of Slicing Is Not Return In Slicing
print (string1[6:9]) # slicing => you (Becuse r Is End Of Slicing)

# if let End is empty will slice to End of String

print (string1[-11:]) # slicing => your school

print (string1[-5]+string1[-3:]) # guess what return

# 2 slicing [start : end : steps]

string2 = "I Love python"

print (string2[0::2]) # slicing =>Ilv yhn 
print ( string1[::3]) # slicing => gtyrco
