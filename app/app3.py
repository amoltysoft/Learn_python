# تمارين deepseek

# 1 
s1 = "Python3"
s2 ="3Python"
s3 = "Python_3"
s4 = " "
s5 = "Python 3"
# s1
print (s1.isidentifier()) # true لانه يمكنك استخدام النص كاسم متغير 
print (s1.isspace()) # false لان النص ليس بمسافة 
print (s1.isalpha()) # false لانه لايحتوي على حروف فقط 
print (s1.isalnum()) # true لانه يحتوي على حروف وارقام 

# s2 
print (s2.isidentifier())  # false لان النص يبدا برقم اي لايمكنك وضعه كاسم متغير
print (s2.isspace()) # false لان النص ليس مسافة 
print (s2.isalpha()) # false لان النص لا يحتوي على حروف فقط
print (s2.isalnum()) # true لانه يحتوي على حروف وارقام 

# s3 
print (s3.isidentifier()) # true لانه يمكن استخدام النص كاسم متغير 
print (s3.isspace()) # false لان النص ليس مسافة 
print (s3.isalpha()) # false لانه لا يحتوي على الحروف فقط 
print (s3.isalnum()) # false لان النص يحتوي على _ وليس حروف وارقام فقط

# s4
print (s4.isidentifier())  # false لان النص عبارة عن مسافة
print (s4.isspace()) # true  لان النص عبارة عن مسافة
print (s4.isalpha()) # false لان النص لا يحتوي سوى على مسافة 
print (s4.isalnum()) # false لانه لا يحتوي سوى على مسافة 

# s5
print (s5.isidentifier()) # false لان النص يحتوي على مسافة 
print (s5.isspace()) #false لانه ليس عبارة عن مسافة فقط 
print (s5.isalpha()) #false لانه يحتوي على مسافة وليس حروف فقط 
print (s5.isalnum())  # false لانه يحتوي على مسافة وليس حروف وارقام

# ملاحظه الاحرف العربية يمكن استخدامها كا سماء متغيرات وايضا تعتبر ضمن alpha
# ملاحظة \t ,\n يعتبرو كامسافات اي اذا طبقت عليهم isspace الناتج true
# حسنا سأحل باقي التمارين واحد تلو الاخر 



