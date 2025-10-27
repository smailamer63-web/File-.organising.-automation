import os
import shutil

FOLDER_PATH = r"C:\Users\YourName\Downloads"

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Music": [".mp3", ".wav", ".aac"],
}

def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print(f"❌ المسار غير موجود: {FOLDER_PATH}")
        return

    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file_name)[1].lower()
        moved = False

        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                target_folder = os.path.join(FOLDER_PATH, category)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f"📁 تم نقل: {file_name} → {category}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(FOLDER_PATH, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"📦 تم نقل: {file_name} → Others")

    print("\n✅ تمت عملية التنظيم بنجاح!")

if __name__ == "__main__":
    organize_files()
