# DenseNet169-Klasifikasi-Batik-DenseNet-169

---

## 🚀 Teknologi & Tools

- Python 🐍  
- TensorFlow / Keras  
- DenseNet-169 
- Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit  

---

## 🧠 Cara Kerja Singkat

1. Dataset dikumpulkan dari berbagai sumber dan diseleksi manual.
2. Dilakukan augmentasi untuk meningkatkan variasi dan ketahanan model.
3. Model dibangun dengan Densenet-169 menggunakan transfer learning (freeze dan data augment skenario).
4. Evaluasi dilakukan dengan *K-Fold Cross-Validation*.
5. Pengujian dilakukan pada data tambahan untuk menguji generalisasi model.

---

## 🎯 Hasil Akhir

Model terbaik diperoleh dari zoom augmentasi, menghasilkan akurasi:
- **98,31%** pada dataset Batik Jawa

---

## 📸 Demo Aplikasi

Tersedia file `Streamlit.py` untuk mencoba langsung klasifikasi gambar batik menggunakan antarmuka Streamlit. Cukup jalankan:

```bash
streamlit run Streamlit.py
