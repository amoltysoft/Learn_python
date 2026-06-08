#--------------------------------------------
#----------Escape sequences characters----------
# \ =>Escape new line + \
# \b =>Back Space =>remove last letter before \b
# \n =>line feed => prints new line
# \\ => prints back slash 
# \' => Escape single quote
# \" => Escape double quotes
# \r  =>carriage Return => cut letter after \r with  before it
# \t  => horizontal tap => prints tap 
# \xhh => character hex value 
#--------------------------------------

# ---- Examples -----

# \ 

print ("name : \
Ali ") # prints name : Ali 

# \b 
print ("this is fore\b you") #remove letter e

#\n 
print ("1-apple\n2-watermalen") 

# \\ 
print ("20\\5 =4")

# \' 
print ('I\'m hothaifa')

#\" 
print ("I am like \"love\" programming")

# \r  note: space is a character
print ("after \rbefore") #prints before

print ("123456\rabcd") #replace 1234 =>abcd

#\t 

print ("this is table for data")
print ("\tName\t ahmad\
\n\tAge\t 26\
\n\tSex\t male\n")

# \xhh 
print ("I am in \x32\x30\x32\x36 ") #I am in 2026 
print ("\x50\x79\x74\x68\x6f\x6e") #python

#End
