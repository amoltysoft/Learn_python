# deepseek (splitlines,rjust,ljust)

# 2 

poem = """يا ليل
الصب متى غده
أيا ساهر
الأنجم راقبها"""

list_line = poem.splitlines() # تحويل النص الى قائمة حيث كل عنصر عبارة عن عنصر في القائمة 

# تحويل العناصر الى متغيرات منفرده 
item1 = list_line[0]
item2 = list_line[1]
item3 = list_line[2]
item4 = list_line[3]

# تصفية الفراغات من الطرفين 
item1 = item1.strip()
item2 = item2.strip()
item3 = item3.strip()
item4 =item4.strip()

# هنا نبدا بالفحص 

#item1
if item1.find(" ") == -1 :
	print (item1.ljust(30))
elif item1.startswith("ا") or item1.startswith("أ") :
	print(item1.rjust(40,"*"))
	
else: 
	print (item1)
	
#item2
if item2.find(" ") == -1 :
	print (item2.ljust(30))
elif item2.startswith("ا") or item2.startswith("أ") :
	print(item2.rjust(40,"*"))
	
else: 
	print (item2)
	
#item3
if item3.find(" ") == -1 :
	print (item3.ljust(30))
elif item3.startswith("ا") or item3.startswith("أ") :
	print(item3.rjust(40,"*"))
	
else: 
	print (item3)
	
#item4
if item4.find(" ") == -1 :
	print (item4.ljust(30))
elif item4.startswith("ا") or item4.startswith("أ") :
	print(item4.rjust(40,"*"))
	
else: 
	print (item4)
	
