import time
import threading
import requests
from datetime import datetime

# ========== الإعدادات (عدّلها حسب جهازك) ==========
TARGET_URL = "http://192.168.133.2/api/change/00000000000?rate=6M&mac=00:11:22:33:44:55"
TEST_DURATION = 10  # مدة الاختبار بالثواني
MAX_THREADS_TO_TEST = [1,3, 5,10,20,30,50, 100, 150 ,200 ,300,350,400]  # عدد الخيوط التي سنختبرها
# =================================================

results = {}
stop_test = threading.Event()

def test_request(thread_id, counter_dict):
    """يرسل طلبات متتالية ويحسبها"""
    local_count = 0
    session = requests.Session()
    while not stop_test.is_set():
        try:
            resp = session.get(TARGET_URL, timeout=2)
            local_count += 1
        except:
            pass
    counter_dict[thread_id] = local_count

def run_test(num_threads):
    """يشغّل اختباراً بعدد معين من الخيوط"""
    global stop_test
    stop_test.clear()
    counters = {}
    threads = []
    
    print(f"\n🔬 اختبار {num_threads} خيط لمدة {TEST_DURATION} ثوانٍ...")
    
    # بدء الخيوط
    for i in range(num_threads):
        t = threading.Thread(target=test_request, args=(i, counters))
        t.daemon = True
        t.start()
        threads.append(t)
    
    # الانتظار للمدة المحددة
    time.sleep(TEST_DURATION)
    stop_test.set()
    
    # انتظار انتهاء جميع الخيوط
    for t in threads:
        t.join(timeout=1)
    
    # حساب النتائج
    total_requests = sum(counters.values())
    requests_per_second = total_requests / TEST_DURATION
    avg_per_thread = requests_per_second / num_threads
    
    results[num_threads] = {
        'total': total_requests,
        'per_second': requests_per_second,
        'per_thread': avg_per_thread
    }
    
    print(f"   ✓ إجمالي الطلبات: {total_requests}")
    print(f"   ✓ طلب/ثانية: {requests_per_second:.1f}")
    print(f"   ✓ طلب/ثانية لكل خيط: {avg_per_thread:.1f}")

def main():
    print("=" * 60)
    print("📊 أداة اختبار أداء هجوم القاموس")
    print("=" * 60)
    print(f"الهدف: {TARGET_URL}")
    print(f"مدة كل اختبار: {TEST_DURATION} ثوانٍ")
    print(f"عدد الخيوط المختبرة: {MAX_THREADS_TO_TEST}")
    print("-" * 60)
    
    # اختبار مبدئي للاتصال
    try:
        resp = requests.get(TARGET_URL, timeout=3)
        print("✅ الراوتر متصل وجاهز.")
    except:
        print("❌ تعذر الاتصال بالراوتر. تأكد من الشبكة.")
        return
    
    # تشغيل الاختبارات
    for num_threads in MAX_THREADS_TO_TEST:
        run_test(num_threads)
        time.sleep(2)  # استراحة بين الاختبارات
    
    # عرض الملخص النهائي
    print("\n" + "=" * 60)
    print("📋 الملخص النهائي:")
    print("-" * 60)
    print(f"{'خيوط':<8} {'إجمالي':<10} {'طلب/ث':<12} {'كفاءة/خيط':<12}")
    print("-" * 60)
    
    best_threads = None
    best_speed = 0
    
    for threads, data in sorted(results.items()):
        total = data['total']
        speed = data['per_second']
        efficiency = data['per_thread']
        marker = ""
        if speed > best_speed:
            best_speed = speed
            best_threads = threads
            marker = " ← الأفضل"
        print(f"{threads:<8} {total:<10} {speed:<12.1f} {efficiency:<12.1f}{marker}")
    
    print("-" * 60)
    print(f"\n🎯 التوصية: استخدم MAX_THREADS = {best_threads}")
    print(f"   (أعلى سرعة: {best_speed:.1f} طلب/ثانية)")
    
    # حساب الوقت المتوقع
    total_possible = 10**11  # كل التركيبات الممكنة لـ 11 رقم
    if best_speed > 0:
        seconds = total_possible / best_speed
        days = seconds / 86400
        print(f"\n⏱️ الوقت المتوقع لفحص كل التركيبات: {days:,.0f} يوم")
        print("   (هذا تقدير نظري، قد تجد كلمة المرور أسرع)")
    
    print("\n💡 نصيحة: استخدم هذا الرقم في كود الهجوم الرئيسي.")

if __name__ == "__main__":
    main()

