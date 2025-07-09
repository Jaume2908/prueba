import streamlit as st

st.title("Formulario de prueba")

# Usamos un formulario para agrupar los inputs y un botón de envío
with st.form("formulario_prueba"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo electrónico")
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    descripcion = st.text_area("Cuéntanos algo sobre ti")

    enviar = st.form_submit_button("Enviar")

if enviar:
    st.success("¡Formulario enviado con éxito!")
    st.write("### Resumen de tu información:")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Correo:** {correo}")
    st.write(f"**Edad:** {edad}")
    st.write(f"**Descripción:** {descripcion}")
