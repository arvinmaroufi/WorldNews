# 🌐 **پروژه خبری `WorldNews` با جنگو**

![home page image](screenshot.png "home page")

## 📋 توضیحات
این پروژه یک سایت خبری است که با استفاده از فریم‌ورک Django ساخته شده است. هدف از این پروژه ارائه یک پلتفرم کاربرپسند برای نمایش اخبار و مقالات مختلف در دسته‌بندی‌های گوناگون می‌باشد.

## 🚀 ویژگی ها

`صفحات اولیه`
- <b>صفحه اصلی: </b>نمایش 7تا خبر از دسته بندی مدنظر، نمایش 4تا از اخبار محبوب و نمایش 5تا از آخرین اخبار
- <b>صفحه تماس با ما: </b>امکان ثبت پیام برای مدیر

`صفحات مربوط به اخبار`
- <b>صفحه لیست اخبار: </b>نمایش تمام اخبار با امکان دکمه "Load More"
- <b>صفحه جزئیات اخبار: </b>نمایش جزئیات اخبار
- <b>صفحه دسته بندی اخبار: </b>نمایش اخبار مربوط به دسته بندی انتخاب شده
- <b>صفحه برچسب اخبار: </b>نمایش اخبار مربوط به برچسب انتخاب شده

`صفحات مربوط به ورود و ثبت نام و پنل کاربران`
- <b>`کاربر`</b>
- <b>سیستم ورود و ثبت نام برای کاربران: </b>امکان ورود و ثبت نام کاربران
- <b>صفحه اصلی پنل کاربری: </b>نمایش پروفایل کاربر
- <b>صفحه ویرایش پروفایل: </b>امکان ویرایش پروفایل برای کاربر
- <b>عملیات خروج کاربر: </b>قابلیت خروج کاربر از حساب
- <b>`مدیر`</b>
- <b>صفحه اصلی پنل کاربری: </b>نمایش پروفایل مدیر
- <b>صفحه اضافه کردن دسته بندی: </b>امکان اضافه کردن دسته بندی
- <b>صفحه اضافه کردن برچسب: </b>امکان اضافه کردن برچسب
- <b>صفحه اضافه کردن اخبار: </b>امکان اضافه کردن خبر
- <b>صفحه لیست دسته بندی ها: </b>نمایش تمام دسته بندی ها با صفحه بندی اصولی و امکان جستجو و ویرایش و حذف آن ها
- <b>صفحه لیست برچسب ها: </b>نمایش تمام برچسب ها با صفحه بندی اصولی و امکان جستجو و ویرایش و حذف آن ها
- <b>صفحه لیست اخبار: </b>نمایش تمام اخبار با صفحه بندی اصولی و امکان جستجو و ویرایش و حذف آن ها
- <b>صفحه لیست پروفایل ها: </b>نمایش تمام پروفایل ها با صفحه بندی اصولی و امکان ویرایش و حذف کامل پروفایل و کاربر
- <b>صفحه ویرایش پروفایل: </b>امکان ویرایش پروفایل برای مدیر
- <b>عملیات خروج مدیر: </b>قابلیت خروج مدیر از حساب

`دیگر امکانات`
- <b>جستجو اخبار: </b>قابلیت جستجوی اخبار براساس عنوان
- <b>عضویت در خبرنامه: </b>امکان عضویت کاربران در خبرنامه

## 🛠️ نصب و راه اندازی
برای نصب و راه‌اندازی این پروژه، مراحل زیر را دنبال کنید:

1. **کلون کردن مخزن:**

```bash
git clone https://github.com/arvinmaroufi/WorldNews.git
cd repo
```

2. **ایجاد محیط مجازی (اختیاری):**

```bash
python -m venv venv
source venv/bin/activate  # برای سیستم‌های Unix/Mac
venv\Scripts\activate  # برای ویندوز
```

3. **نصب وابستگی‌ها:**
   
```bash
pip install -r requirements.txt
```

4. **اجرای migrations:**

```bash
python manage.py migrate
```

5. **اجرای سرور:**

```bash
python manage.py runserver
```

6. **دسترسی به وب‌سایت:**
   در مرورگر خود به آدرس http://127.0.0.1:8000/ بروید.

## ✅ استفاده

پس از راه‌اندازی، می‌توانید پروژه رو مشاهده کنید و لذت ببرید.

## 🎯 مشارکت

اگر تمایل به مشارکت در این پروژه دارید، لطفاً مراحل زیر را دنبال کنید:

1. یک فورک از مخزن ایجاد کنید.
2. تغییرات خود را اعمال کنید.
3. یک Pull Request ارسال کنید.

## 🧾 مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## 💻 برنامه نویس

**آروین معروفی** - [لینک پروفایل گیت‌هاب](https://github.com/arvinmaroufi)

## 💬 ارتباط با ما

اگر سوالی دارید یا نیاز به کمک بیشتری دارید، لطفاً با ما تماس بگیرید:

- **ایمیل**: [arvinmaroufi.dev@gmail.com](mailto:arvinmaroufi.dev@gmail.com)
- **گیت‌هاب**: [arvinmaroufi](https://github.com/arvinmaroufi/arvinmaroufi/issues)
- **اینستاگرام**: [arvinmaroufi.ir](https://instagram.com/arvinmaroufi.ir)
- **تلگرام**: [arvin_maroufi](https://t.me/arvin_maroufi)

ما خوشحال می‌شویم که از شما بشنویم 🙏

## ❤️ حمایت از ما

اگر از کار ما لذت می‌برید و می‌خواهید از ما حمایت کنید، لطفاً ما را در شبکه‌های اجتماعی دنبال کنید:

- **گیت‌هاب**: [arvinmaroufi](https://github.com/arvinmaroufi)
- **اینستاگرام**: [arvinmaroufi.ir](https://instagram.com/arvinmaroufi.ir)
- **تلگرام**: [arvinmaroufi_ir](https://t.me/arvinmaroufi_ir)

از حمایت شما سپاسگزاریم 🙏