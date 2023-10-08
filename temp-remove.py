import os
import shutil

def delete_contents(directory):
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    print(f"Skipped: {item_path} (not a file or folder)")
            except PermissionError as pe:
                print(f"Skipped: {item_path} (PermissionError: {str(pe)})")
            except Exception as e:
                print(f"Skipped: {item_path} ({str(e)})")
    except Exception as e:
        print(f"An error occurred while listing contents of {directory}: {str(e)}")

# Specify the directories you want to delete files and folders from
directories_to_clean = [
    r"C:\Users\YOUR-USER\AppData\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\Prefetch",
    r"C:\$Recycle.Bin"
]

for directory in directories_to_clean:
    delete_contents(directory)
