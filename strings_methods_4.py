#-----------------------------------------------
# ----------------strings method 4 --------------
# var.replace(oldvalue , newvalue , count ) => replace old value with new value by count 
# seperator.join(list) => change lists or tuple to string and join it  with seperator 
#--------------------------


# EXAMPLES

# var.replace(old,new,count)

date_words = "tow zero tow six"

date_digit= date_words.replace("tow ","2") # if not add count will replace all
date_digit = date_digit.replace("zero ","0")
date_digit = date_digit.replace("six", "6")
print (date_words)
print (date_digit)

str1 = "one tow three one tow tow "

print(str1.replace("tow" , "2" , 2))

# seperator.join(list)

list_words = ["i","love","python"]
print(list_words)
print (" ".join(list_words))
print ("_".join(list_words))
print ("-".join(list_words))



