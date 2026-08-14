from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform
from kivy_garden.mapview import MapView, MapMarker, MapSource

# مختصات مرکز شهر اصفهان
ISFAHAN_LAT = 32.6546
ISFAHAN_LON = 51.6680

class IsfahanMapApp(App):
    def build(self):
        # چیدمان اصلی صفحه به صورت عمودی
        self.layout = BoxLayout(orientation='vertical')

        # ۱. ساخت نقشه و تنظیم زوم و مختصات اولیه روی اصفهان
        self.mapview = MapView(
            zoom=13, 
            lat=ISFAHAN_LAT, 
            lon=ISFAHAN_LON
        )
        
        # در صورت تمایل به تغییر منبع نقشه یا افزودن لایه اختصاصی اسوپ اصفهان:
        # custom_source = MapSource(url="https://esup.isfahan.ir/tiles/{z}/{x}/{y}.png")
        # self.mapview.map_source = custom_source

        self.layout.add_widget(self.mapview)

        # ۲. ایجاد نشانگر (Marker) اولیه روی نقشه
        self.user_marker = MapMarker(lat=ISFAHAN_LAT, lon=ISFAHAN_LON)
        self.mapview.add_widget(self.user_marker)

        # ۳. دکمه درخواست موقعیت مکانی (GPS)
        self.btn_gps = Button(
            text="Find My Location (GPS)", 
            size_hint_y=0.12
        )
        self.btn_gps.bind(on_press=self.start_gps)
        self.layout.add_widget(self.btn_gps)

        return self.layout

    def start_gps(self, instance):
        # بررسی اجرای برنامه روی سیستم‌عامل اندروید
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            # درخواست دسترسی‌های GPS از کاربر
            request_permissions([
                Permission.ACCESS_FINE_LOCATION, 
                Permission.ACCESS_COARSE_LOCATION
            ], self.permission_callback)
        else:
            print("سرویس GPS فقط روی دستگاه اندرویدی فعال می‌شود.")

    def permission_callback(self, permissions, grant_results):
        # اگر کاربر دسترسی داد، سرویس GPS روشن می‌شود
        if all(grant_results):
            try:
                from plyer import gps
                gps.configure(on_location=self.on_location)
                gps.start(minTime=1000, minDistance=1)
            except Exception as e:
                print(f"خطا در راه اندازی GPS: {e}")

    def on_location(self, **kwargs):
        # دریافت مختصات جدید و به‌روزرسانی نقشه
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        if lat and lon:
            self.user_marker.lat = lat
            self.user_marker.lon = lon
            self.mapview.center_on(lat, lon)

if __name__ == '__main__':
    IsfahanMapApp().run()
