
# هذا تطبيق حسابات الفرنسي انتاج الوارثي سوفت
# استيراد المكاتب
import time

# عمل قائمة بالايام العربية
days_ar = ["الاثنين", "الثلاثاء","الاربعاء","الخميسا","الجمعة","السبت","الاحد"]
day = time.localtime()
# الحصول على اليوم للاسبوم زيبدا بيوم الاثنين ورقمه 0 
index_days =day.tm_wday
# استخدام رقم اليوم كافهرس للقائمة
day_ar = days_ar[index_days]

date = time.strftime("%Y/%m/%d")

shirts = input("كم اشتغلت شمزان: "[::-1])
pants1 = input("كم اشتغلت بناطيل: "[::-1])
skirt = input("مك اشتغلت مرايل: "[::-1])
cut = input("كم معك قصة: "[::-1])
pants2 = input ("كم اشتغلت سراويل: "[::-1])
bag = input("كم معك شنط"[::-1])
cash = input ("كم معك مصروف: "[::-1])
who = input(" :من جابلك المصروف"[::-1])
#تنسيق النتائج 

div = f"""\n
اليوم:{day_ar}\t\tالتاريخ: {date}
---------------------------------
  {shirts} = شمزان\n {pants1} = بناطيل\n{skirt} = مرايل\n{cut} = قصة\n{pants2} = سراويل\n{bag} = شنط \n{cash} = المصروف\n{who} = من المصروف
"""
with open ("../../storage/shared/a.txt","a",encoding="utf-8")as file:
	file.write(div+"="*40)
