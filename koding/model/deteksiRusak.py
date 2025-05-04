import os
import shutil
from PIL import Image

def detect_non_image(dataset_folder):
    non_images = []
    os.makedirs(destination_folder, exist_ok=True)
    report = {}
    
    for label in os.listdir(dataset_folder):
        label_folder = os.path.join(dataset_folder, label)
        if os.path.isdir(label_folder):
            initial_count = len(os.listdir(label_folder))
            deleted_count = 0
            
            for filename in os.listdir(label_folder):
                file_path = os.path.join(label_folder, filename)
                try:
                    with Image.open(file_path) as img:
                        img.verify()
                except (IOError, SyntaxError) as e:
                    non_images.append(file_path)
                    print(f"File tidak valid atau rusak: {file_path}")
                    try:
                        shutil.move(file_path, destination_folder)
                        print(f"File moved to: {destination_folder}")
                        deleted_count += 1
                    except shutil.Error as e:
                        print(f"Error moving file {file_path}: {e}")
            
            final_count = initial_count - deleted_count
            report[label] = {
                "initial_count": initial_count,
                "deleted_count": deleted_count,
                "final_count": final_count
            }
    
    for label, stats in report.items():
        print(f"{label}: {stats['initial_count']} awal, {stats['deleted_count']} dihapus, {stats['final_count']} akhir")
    
    return non_images

dataset_folder = r'C:\Users\ASUS\OneDrive - Duta Wacana Christian University\Documents\8th semester\Skripsi\koding\dataset\Dataset Batik Jawa' # path folder dataset Anda
destination_folder = r'C:\Users\ASUS\OneDrive - Duta Wacana Christian University\Documents\8th semester\Skripsi\koding\dataset\Data Rusak' # path folder tujuan Anda
detect_non_image(dataset_folder)