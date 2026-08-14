[app]

# نام برنامه روی گوشی
title = Isfahan Map

# نام پکیج (بدون فاصله و حروف بزرگ)
package.name = isfahanmap
package.domain = org.isfahan.app

# مسیر سورس کد
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# نسخه برنامه
version = 0.1

# کتابخانه‌های مورد نیاز پایتون
requirements = python3,kivy==2.2.1,kivy_garden.mapview,plyer,requests,urllib3

# حالت نمایش (عمودی)
orientation = portrait

# دسترسی‌های مورد نیاز اندروید
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# تنظیمات نسخه اندروید
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
