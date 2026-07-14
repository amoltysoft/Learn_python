# اخذ البيانات من المستخدم 
# الحصول على الاسم 
name = input("enter your name: ")

#الحصول على العمر
age = input("type your age: ")

# الحصول على  الطول 

hieght = float(input ("type your hieght: "))

# اذا ادخل المستخدم الطول بالسنتيمتر 
if hieght >= 2.75 :
	hieght = hieght/100
	
print ("hi is {:.2f}".format(hieght))
