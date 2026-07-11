#---------------------------
#------- numbers  --------
# There 3 types of numbers in python 
# 1) int => integer 
# 2) float => floatting point numbers
# 3) complex => complex have 2 parts (reall number,imaginary number)
# the part of imaginary ends with  latter j
# you can format complex number
# you can convert from int to float or complex 
# you can convert from float to int or complex 
# you can't convert from complex to int or float 




#EXAMPLES

# integer 

print (type(100)) # integer
print (type(20)) # integer
print (type(-50)) # integer
print (type(-3000)) # integer


# floatting point number

print (type(10.66))
print (type(106.6))
print (type(-19.66))
print (type(-10.66))

# complex

print (type(66+6j))
print (type(10+66j))
print (type(-160.66+66j))




# you can format 
num_complex = 12+77j
print (num_complex)

# print part real
print ("part real is {}".format(num_complex.real))
print (f"part imaginary is {num_complex.imag}")


# you can convert from int to float or complex

num1 = 12

print (float(num1)) # prints 12.0 
print (complex(num1)) # prints 12+0j


# you can convert from float to int or complex 

num2 = 3.14

print (int(num2)) # prints 3

print (complex(num2)) # prints 3.14+0j


# you can't convert from complex to any athor type

num3 = 10+5j
#print (int(num3)) # get erorr
#print (float(num3)) # get erorr
