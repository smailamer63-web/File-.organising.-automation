# 🗂️ File Organizer Automation

مشروع بسيط بلغة **Python** يقوم بترتيب الملفات تلقائيًا داخل مجلد معين حسب نوعها  
(صور – فيديوهات – مستندات – ملفات مضغوطة – صوتيات – أخرى).

---

## 🚀 طريقة التشغيل

1. قم بتنزيل الكود أو نسخه.
2. عدّل المسار داخل الكود إلى مجلدك (مثلاً مجلد التنزيلات):
   ```python
   FOLDER_PATH = r"C:\Users\YourName\Downloads"
   ```
3. شغّل السكريبت:
   ```bash
   python main.py
   ```
4. سيتم إنشاء مجلدات فرعية تلقائيًا (Images, Videos, Documents, Archives, Music, Others).

---

## 🧰 المتطلبات
- Python 3.8 أو أحدث  
- لا تحتاج إلى مكتبات إضافية (يعمل فقط بـ os و shutil)

---

## 📸 مثال عملي
قبل:
```
Downloads/
├── photo.jpg
├── resume.pdf
├── video.mp4
```

بعد التشغيل:
```
Downloads/
├── Images/photo.jpg
├── Documents/resume.pdf
├── Videos/video.mp4
```

---

## 💡 أفكار للتطوير
- جعل السكريبت يعمل تلقائيًا كل فترة زمنية.
- إضافة واجهة رسومية بسيطة (GUI).
- دعم اللغات المتعددة.
- رفع إشعارات عند التنظيم التلقائي.

---

✦ **Made with ❤️ by [YourName]**
