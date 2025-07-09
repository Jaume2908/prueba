import streamlit as st
from PIL import Image

st.title("Formulario desde el móvil 📱")

with st.form("form_movil"):
    nombre = st.text_input("Nombre")
    imagen = st.file_uploader("Sube una foto (galería o cámara)", type=["jpg", "jpeg", "png"])

    enviado = st.form_submit_button("Enviar")

if enviado:
    st.success("¡Formulario enviado con éxito!")
    st.write(f"**Nombre:** {nombre}")

    if imagen:
        img = Image.open(imagen)
        st.image(img, caption="Imagen subida", use_column_width=True)
    else:
        st.warning("No se ha subido ninguna imagen.")

