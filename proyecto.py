import streamlit as st

st.set_page_config(page_title="Mision Salta", page_icon="💜")

st.title("Mision Salta")

nombre=st.text_input("¿Cuál es tu nombre")

MODELOS = ("fotos", "videos", "cafecito")

if st.button("Confirmar!"):
    st.write(f"¡Hola {nombre}, gracias por interesarte en la Mision Salta")
def configurar_pagina():
    st.title("Mision Salta")
    st.sidebar.title("opciones")
    opcion = st.sidebar.selectbox(
        "Elegí modelo", #titulo
        options = MODELOS, #opiciones deben estar en una lista
        index = 0 #valorPorDefecto
   )
def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model = modelo, 
        messages = [{"role":"user", "content" : mensajeDeEntrada}];
        stream = True,   
    )
           
        

def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append(
        {"role:": rol, "content": contenido, "avatar": avatar}
    )
def mostrar_historia():
    for mensaje in st.session_state.mensajes:
       with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]):
             st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height= 400, border= True)
    with contenedorDelChat: mostrar_historia()

def generar_respuesta(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        print(frase.choices[0].delta.content)
        if frase.choices[0].delta.content:
            respuesta_completa += frase.choices[0].delta.content
            yield frase.choices[0].delta.content
    return respuesta_completa

def main():
    #? INVOCACION DE FUNCIONES
    modelo = configurar_pagina()
    area_chat()
    mensaje = st.chat_input

    if mensaje:
        actualizar_historial("user", mensaje, "👦🏻")

        if chat_completo:
            with st.chat_message("assistant"):
                respuesta_completa = st.write_stream(generar_respuesta(chat_completo))
                actualizar_historial("assistant", respuesta_completa, "🤖")
                st.rerun()

if __name__ == "__main__":
    main()

mensaje = st.chat_input("Haz una pregunta de la Mision...")