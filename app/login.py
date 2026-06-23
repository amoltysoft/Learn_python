# deepseek login

# logo
#logo = "مدقق اسم المستخدمين وكلمة المرور "
#print (logo.center(len(logo)+12,"-")+"\n")

#سنطلب من المستخدم ان يدخل اسم مستخدم وكلمة مرور 
user_name = input("ادخل اسم المستخدم : ")

password = input("ادخل كلمة المرور : ")


# فلترة اسم المستخدم 

if " " in user_name: # فلترة المسافة 
	if user_name.isidentifier(): #هل هو كمعرف او لا
		if len(user_name) >=5 and len(user_name) <=15: # طول الاسم يكون بين ٥ و١٥ 
			if user_name[0].isalpha: #هل يبدا بحرف 
				if user_name.isalnum():#هل يحتوي على حروف وارقام 
					user = user_name 
					
				else:
					print ("يجب ان يحتوي اسم المستخدم على حروف وارقام فقط ")
					
			else:
				print ("يجب ان يبدا اسم المستخدم بحرف فقط ")
		else :
			print ("يجب ان يكون اسم المستخدم مابين 5حروف الى 15حرفا فقط ")
	else :
		print ("يجب ان يكون اسم المستخدم كمعرف ")
else :
	print ("يجب ان لا يحتوي اسم المستخدم على مسافات ")




	
		
				
					
	