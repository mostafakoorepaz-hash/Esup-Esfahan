[app]

# نام برنامه روی گوشی
title = Isfahan Map

# نام پکیج (بدون فاصله، اعداد یا حروف بزرگ)
package.name = isfahanmap

# دامنه پکیج
package.domain = org.isfahan.app

# مسیر فایل‌های سورس پروژه
source.dir = .

# پسوند فایل‌هایی که باید در پکیج قرار گیرند
source.include_exts = py,png,jpg,kv,atlas

# نسخه برنامه
version = 0.1

# کتابخانه‌های مورد نیاز پایتون
requirements = python3,kivy==2.2.1,kivy_garden.mapview,plyer,requests,urllib3

# حالت نمایش برنامه (عمودی)
orientation = portrait

# دسترسی‌های مورد نیاز اندروید (اینترنت و GPS)
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# تنظیمات نسخه API اندروید
android.api = 33
android.minapi = 21
android.ndk = 25b

# پذیرش خودکار لایسنس‌های اندروید
android.accept_sdk_license = True

# معماری پردازنده گوشی‌های مدرن اندروید
android.archs = arm64-v8a

# شاخه اصلی python-for-android
p4a.branch = master


[buildozer]

# سطح لاگ گرفتن (برای مشاهده جزئیات خطاهای احتمالی)
log_level = 2

# هشدار در صورت اجرا به عنوان کاربر root
warn_on_root = 1
