import os
import shutil
import schedule
import time

def auto_sort():
    import os
    import shutil
    import schedule
    import time

    path = r'C:/Users/HP/Downloads/'
    file_name = os.listdir(path)
    folder_names = ['General Documents (Automatic)', 'PDF Documents (Automatic)', 'Images (Automatic)', 'Music & Videos (Automatic)', 'Excel & CSV Datasets (Automatic)', 'Programs (Automatic)', 'Compressed (Automatic)']

    for loop in range(0,6):
        if not os.path.exists(path + folder_names[loop]):
            print(path + folder_names[loop])
            os.makedirs(path + folder_names[loop])

    for file in file_name:
        if '.docx' in file and not os.path.exists(path + 'General Documents (Automatic)/' + file):
            shutil.move(path + file, path + 'General Documents (Automatic)/' + file)
        elif '.doc' in file and not os.path.exists(path + 'General Documents (Automatic)/' + file):
            shutil.move(path + file, path + 'General Documents (Automatic)/' + file)
        elif '.pptx' in file and not os.path.exists(path + 'General Documents (Automatic)/' + file):
            shutil.move(path + file, path + 'General Documents (Automatic)/' + file)
        elif '.pdf' in file and not os.path.exists(path + 'PDF Documents (Automatic)/' + file):
            shutil.move(path + file, path + 'PDF Documents (Automatic)/' + file)
        elif '.jpeg' in file and not os.path.exists(path + 'Images (Automatic)/' + file):
            shutil.move(path + file, path + 'Images (Automatic)/' + file)
        elif '.jpg' in file and not os.path.exists(path + 'Images (Automatic)/' + file):
            shutil.move(path + file, path + 'Images (Automatic)/' + file)
        elif '.png' in file and not os.path.exists(path + 'Images (Automatic)/' + file):
            shutil.move(path + file, path + 'Images (Automatic)/' + file)
        elif '.webp' in file and not os.path.exists(path + 'Images (Automatic)/' + file):
            shutil.move(path + file, path + 'Images (Automatic)/' + file)
        elif '.mp3' in file and not os.path.exists(path + 'Music & Videos (Automatic)/' + file):
            shutil.move(path + file, path + 'Music & Videos (Automatic)/' + file)
        elif '.mp4' in file and not os.path.exists(path + 'Music & Videos (Automatic)/' + file):
            shutil.move(path + file, path + 'Music & Videos (Automatic)/' + file)
        elif '.mkv' in file and not os.path.exists(path + 'Music & Videos (Automatic)/' + file):
            shutil.move(path + file, path + 'Music & Videos (Automatic)/' + file)
        elif '.csv' in file and not os.path.exists(path + 'Excel & CSV Datasets (Automatic)/' + file):
            shutil.move(path + file, path + 'Excel & CSV Datasets (Automatic)/' + file)
        elif '.xlsx' in file and not os.path.exists(path + 'Excel & CSV Datasets (Automatic)/' + file):
            shutil.move(path + file, path + 'Excel & CSV Datasets (Automatic)/' + file)
        elif '.sql' in file and not os.path.exists(path + 'Excel & CSV Datasets (Automatic)/' + file):
            shutil.move(path + file, path + 'Excel & CSV Datasets (Automatic)/' + file)
        elif '.exe' in file and not os.path.exists(path + 'Programs (Automatic)/' + file):
            shutil.move(path + file, path + 'Programs (Automatic)/' + file)
        elif '.rar' in file and not os.path.exists(path + 'Compressed (Automatic)/' + file):
            shutil.move(path + file, path + 'Compressed (Automatic)/' + file)
        elif '.zip' in file and not os.path.exists(path + 'Compressed (Automatic)/' + file):
            shutil.move(path + file, path + 'Compressed (Automatic)/' + file)

schedule.every(24).hours.do(auto_sort)

while True:
    schedule.run_pending()
    time.sleep(120)  # Sleep for 2 minutes to avoid high CPU usage