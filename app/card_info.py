#١ البطاقه التعريغية 
# اخذ البيانات من المستخدم 
# الحصول على الاسم 
name = input("enter your name: ")

#الحصول على العمر
age = int(input("type your age: "))

# الحصول على  الطول 

hieght = float(input ("type your hieght: "))

# اذا ادخل المستخدم الطول بالسنتيمتر 
if hieght >= 2.75 :
	hieght = float(hieght/100)
	

print ("مرحبا{:s} عمرك هو{:d} وطولك هو {:.2f} متر".format(name.capitalize(),age,hieght))

