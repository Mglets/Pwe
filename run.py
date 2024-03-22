import tkinter as tk
from PIL import ImageTk, Image

# إنشاء نافذة التطبيق
window = tk.Tk()
window.title("mo3az sahahen ")
window.geometry("300x300")

# قراءة صورة البومة
image_path = "m.png"  # قم بتغيير اسم الملف وفقًا لمسار الصورة الخاصة بك
image = Image.open(image_path)
image = image.resize((200, 200))  # تغيير حجم الصورة حسب الحاجة
photo = ImageTk.PhotoImage(image)

# عرض الصورة في عنصر الصورة
label = tk.Label(window, image=photo)
label.pack()

# إضافة اسم "Azazel Al-Fayoumie" تحت الصورة
artist_name = "Azazel Al-Fayoumie"
artist_name_label = tk.Label(window,