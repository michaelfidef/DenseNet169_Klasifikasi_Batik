import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
# from tensorflow.keras.applications.densenet import preprocess_input

# Load model yang sudah dilatih
# model = tf.keras.models.load_model("./dense clean/keras aug/rotate/rotate_model_2.keras")

# clear 4 bisa baca
# model = tf.keras.models.load_model("./dense clean/keras aug/zoom+elastic/gabungan_model_4.keras")
# model = tf.keras.models.load_model("./dense clean/keras aug/zoom+rotate/gabungan_model_4.keras")

# model = tf.keras.models.load_model("./dense clean/keras aug/zoom+elastic+rotate/gabungan_model_1.keras")
model = tf.keras.models.load_model("./dense clean/keras aug/zoom in/A2/zoom_model_5.keras")
# model = tf.keras.models.load_model("./dense clean/keras aug/zoom in/A2/150_model_4.keras")

# model = tf.keras.models.load_model("./dense clean/model P2/best_model_5.keras")
# model = tf.keras.models.load_model("./dense clean/keras aug/elastic/Elastic_Model.keras")

# model = tf.keras.models.load_model("./dense clean/keras/conv5_model_2.keras")
# model = tf.keras.models.load_model("./dense clean/keras/150_model_5.keras")
# model = tf.keras.models.load_model("./dense clean/keras/50_model_5.keras")
# model = tf.keras.models.load_model("./dense clean/model P2/best_model_5.keras")

# Daftar label kelas
class_labels = ["Kawung", "Mega Mendung", "Parang", "Truntum"]

def preprocess_image(image):
    """Mengubah gambar menjadi array yang sesuai dengan input model."""
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (224, 224)) 
    image = image / 255.0 
    
    image = np.expand_dims(image, axis=0)
    
    return image

# Fungsi prediksi
def predict(image):
    """Melakukan prediksi menggunakan model yang telah dimuat."""
    processed_image = preprocess_image(image)  # Preprocessing gambar
    predictions = model.predict(processed_image)[0]  # Prediksi

    probabilities = {class_labels[i]: float(predictions[i]) for i in range(len(class_labels))}
    predicted_class = max(probabilities, key=probabilities.get)
    confidence = probabilities[predicted_class] * 100 

    return probabilities, predicted_class, confidence

# Streamlit UI
st.title("Klasifikasi Motif Batik dengan DenseNet169")
uploaded_file = st.file_uploader("Unggah Gambar Batik", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Konversi PIL image ke array NumPy sebelum diproses
    image_np = np.array(image)
    st.image(image, caption="Gambar Batik yang Diupload", use_container_width=True)
    probabilities, predicted_class, confidence = predict(image_np)

    st.subheader("Prediksi Probabilitas:")
    for class_name, prob in probabilities.items():
        st.write(f"{class_name}: {prob:.2f}%")

    st.subheader(f"Prediksi Akhir: **{predicted_class}** ({confidence:.2f}%)")
