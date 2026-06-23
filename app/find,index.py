# deepseek (find,index)
# نطلب من المستخدم ادخال جملة 
string_user = input ("اكتب جملة معينة : ")
#نطلب من المستخدم كلمة بحث للبحث عنها 
search_user = input ("ابحث عن كلمة :")

# find هنا نستخدم  دالة 

findit = string_user.find(search_user)
if findit >=0 :
	print ("موجودة بالفعل في موضع "+str(findit))
else :
	print ("الكلمة غير موجوده ")


# index هنا نستخدم دالة 

# هذه الداله الشرطية لتفادي ظهور الخطا عند استخدام دالةindex حتى لا يتوقف باقي الكود 

if search_user in string_user :
	indexit = string_user.index(search_user )
	print ("found in index "+str(indexit))
else :
	print ("لايمكن استخدام دالة index لان الكلمة غير موجودة ")



