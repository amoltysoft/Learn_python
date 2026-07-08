#app with deepseek
#انا لم ادرس القوائم بعد ولكن دعني احاول 
#البيانات القادمة من الطالب 
name = input("ادخل الاسم كاملا :")
age = input("ادخل عمرك: ")
degry =input("ادخل درجتك من٠الى ١٠٠:")
email =input("البريد الالكتروني :")


#عمليات التنسيق
name =name.strip()
start_latter = name[0]
#التحقق من العمر 
while not age.isdigit():
    
    print ("اعد كتابة العمر بالارقام ")
    age =input ("الرجاء كتابة العمر بشكل صحيح ")
    
    



# التحقق من حالة النجاح 
a =True
while a:
    if type(degry) ==int :
        if degry >= 60 and degry <= 100 :
            status = "ناجح"
            a =False
        elif degry <=59 and degry >= 0:
            status = "راسب "
            a =False
        
        else:
            degry = input("ادخل الدرجة من 0 الى 100 ")
            degry =int(degry)
        
        
    else:
        print("ادخل قيمة عدديه")
        degry =input ("ادخل الدرجات بالعدد")
        if degry.isdigit():
            degry =int(degry)
        
            
   
        
#انتهينا من فحص العمر والدرجات ولكن بقي القليل للتحقق من العمر 
#بيانات التقرير 
data = ["حرف", "الاسم","العمر" ,"الدرجات","الحالة","البريد الالكتروني ","نهاية البريد"]

print ("تقرير بيانات الطالب".center(30,"="))

print ()
