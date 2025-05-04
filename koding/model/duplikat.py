import os
import hashlib
import shutil

from PIL import Image

def remove_duplicates(dataset_folder):
    report = {}
    os.makedirs(destination_folder, exist_ok=True)
    for label in os.listdir(dataset_folder):
        label_folder = os.path.join(dataset_folder, label)
        if os.path.isdir(label_folder):
            image_hashes = {}
            initial_count = len(os.listdir(label_folder))
            deleted_count = 0
            for file_name in os.listdir(label_folder):
                file_path = os.path.join(label_folder, file_name)
                try:
                    with Image.open(file_path) as img: img_hash = hashlib.md5(img.tobytes()).hexdigest()
                    if img_hash in image_hashes:
                        deleted_path = os.path.join(destination_folder, file_name)
                        shutil.move(file_path, deleted_path)  # Memindahkan ke folder deleted_duplicates 
                        # os.remove(file_path)
                        deleted_count += 1
                    else:
                        image_hashes[img_hash] = file_name
                except Exception as e:
                    print(f"Gagal memproses '{file_name}': {e}")
            final_count = initial_count - deleted_count
            report[label] = {
            "initial_count": initial_count,
            "deleted_count": deleted_count,
            "final_count": final_count
            }
    for label, stats in report.items():
        print(f"{label}: Data Awal: {stats['initial_count']}, duplikasi: {stats['deleted_count']}, Hasil Akhir: {stats['final_count']}")

# Example usage
dataset_folder = r'C:\Users\ASUS\OneDrive - Duta Wacana Christian University\Documents\8th semester\Skripsi\koding\dataset\augmentasi\zoom in' # path folder dataset Anda
destination_folder = r'C:\Users\ASUS\OneDrive - Duta Wacana Christian University\Documents\8th semester\Skripsi\koding\dataset\duplikat_coba' # path folder tujuan Anda
remove_duplicates(dataset_folder)