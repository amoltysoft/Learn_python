poem = """ألا ليت شعري
هل يدرين ما أخذوا
فلولا الهوى
ما ذلت في الأرض شجرة"""

# تحويل النص الى قائمة ابيات 
list_poem = poem.splitlines()

# حذف الفراغات الطرفية ان وجدت 

item1 = list_poem[0].strip()
item2 = list_poem[1].strip()
item3 = list_poem[2].strip()
item4 = list_poem[3].strip()

# تحويل الابيات الى قائمة مر ةاخرى
list_poem = [item1,item2,item3,item4] 
num =1
print("تقرير التحليل".center(40,"="))
for i in list_poem:
    
    #تحويل الالابيات الى قائمة كلمات 
    words = i.split()
    #الحصول على عدد الكلمات في كل بيت 
    count = len(words)
    
    #الحصول على اول واخر كلمة في كل بيت
    frist_word, last_word = words[0] , words[-1]
    # التحقق من ان البيت يبدا بحرف 
    if i[0].isalpha():
       start = "نعم"
       #هل البيت كله حروف ام ل
       if i.isalpha():
          #التحقق اذا كانت البيت تحتوي     على احرف فقط
            type_alpha = "نعم "# التحقق اذا كانت البيت الشعري حروف صغيرة 
            if i.islower():
                type_latter = "احرف صغيرة"
      #التحقق اذا كانت البيت كاترويسة 
            elif i.istitle( ):
                 type_latter = "كاترويسة"
                 
            else:
                 type_latter = "مختلطة "
       else:
           type_alpha = " لا"
    else:
        start = "لا"
   
    print("البيت رقم\t %s\n" %str(num).zfill(2))
    print ("عددكلمات البيت\t%d\n"%count)
    print("البيت تبدا بحرف ؟\t%s\n"%start)
    print("البيت حروف فقط ؟\t%s"%type_alpha)
    if type_alpha == "نعم ":
        print("نوع البيت ؟\t%s"%type_latter)
        
    
    print ("مضمون البيت:\t%s"%i)
    #التحقق من وجود كلمة الهوي في اي بيت 
    if not i.find("الهوى") ==-1:
        print ("الكلمة موجوده في البيت رقم :%s"%str(num).zfill(2))
        
    print("*".center(50,"*"))
    num+=1
    
        