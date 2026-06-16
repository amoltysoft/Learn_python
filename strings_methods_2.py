# -------------------------------------------------
# ------strings method 2------------------------------------
# var.split()=> change string to list and cut it by whitespace
# var.split(sepr) => like split but cut it by sepr
# var.split(sepr ,mxsplit) => like split(sepr)but will cut to mxsplit items and other item put it in 1 item 
# var.rsplit(sepr ,mxsplit) =>  like split but from end
# var.center(len,char) => put your string between char
# len => lenth of string after center() 
# char => the character you want to put your string between them 
# char by defuilt is whitespace 
# var.count(word) => cout word how many is in var
# var count (word , startpos, endpos) =>like count 
# startpos =>start position 
# endpos =>end position
# var.swapcase() => reversing  status case
# var.startswith(char,startpos,endpos) => search if string start with [char] returns boolean value 
# var.endswith(char,startpos,endpos) => search if string ends with [char] return  boolean value



# EXAMPLES

# var.split()
str1 = "apple banana orange watermalen strawbarry "
listFruit = str1.split() # cut by whitespace
print ("fruits = ",listFruit)

# var.split(sepr)
str2 = "Rasheed ,Ahmed ,Mohammed ,Sadam ,Meqdad ,Nizar ,hothiafa  "
myFamily = str2.split(",") # cut by comma
print ("my brothers = ",myFamily)
# var.split(sepr,mxsplit)

str3 = "Ali_Ahmed_where_are_you_?"

names = str3.split("_",2) # cut 2 item from strintg by _ and put athor in 3rd  item 

print (names)


# var.rsplit(sepr , mxsplit)
str4 = "what your sex ? male female else"

yourSex = str4.rsplit(" ",3)

print (yourSex)

# var.center(len,char)

logo = "alwarithy"
lenth = len(logo) # get logo's lenth
logoUpper = logo.upper() # Change logo to Uppercase 
LOGO = logoUpper.center(lenth+6,"👉" )

print (LOGO)

# var.count(word) casesansitive
str5 = "I love python and php becuse php is easy"

countPhp = str5.count("php")
print (countPhp)


# var.count(word,startpos,endpos) casesansitive
str6 ="""
php is language excute in server and
i love python  and php becuse php is easy
and I'm learning theme
"""

lenth = len(str6) # get lenth of string 
countPhp = str6.count("php",10,lenth-1)

print (countPhp)

countLine = str6.count("\n") # how many line in string
print (countLine) # print it 


# var.swapcase()
str7 = "i lOVE pYTHON" 
print (str7.swapcase())

# var.startwith(char) casesansitive
name = "Alwarithysoft"
print (name.startswith("A")) # if name starts with A will print True

# var.endswith(char,startpos,endpos)

str8 = "I Love Python"
print(str8.endswith("ve",0,6))

