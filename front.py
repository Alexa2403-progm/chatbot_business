import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from business_info import info

st.title('👩‍💻 Asistente TecnoLogiStore')

# Variables de estado
if "messages" not in st.session_state:
    st.session_state.messages = [] #Almacenara el historico del chat
if "first_message" not in st.session_state:
    st.session_state.first_message = True 
    #Sabes si es la 1ra vez que se inicia la aplicacion que inicia en true y cuando se muestre el msj pasara a false


# Recorremos el array de msj para ver si tenemos algo en el historico y mostrarlo en el chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # usamos el metodo chat_message para decirle el role hay dos tipos de role, 1-role-asistente y 2-role-usuario
        # st.markdown(message["content"]) muestra el contenido del msj

# Si es la primera vez que se inicia la aplicacion mostramos un msj de bienvenida.
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("¡Hola! ¿En qué puedo ayudarte?")
    st.session_state.messages.append({"role": "assistant", "content": "¡Hola! ¿En qué puedo ayudarte?"}) # st.session_state.messages.append agrega el msj al historico del chat con append
    st.session_state.first_message = False    

# Por ultimo reaccionar a un msj que nos escriba el usuario a traves del promt, streamlit tiene este metodo para crear el promt "chat_input("lo que quieres que aparezca") * movido a la linea 59 

  

if "ollama" not in st.session_state:

    template = """
    Answer the question below in Spanish.

    Here is the business information:
    {business_info}

    {context}

    Question: {question}

    Answer:

    """

    model = OllamaLLM(model="gemma3")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    context = ""



if prompt := st.chat_input("¿Como puedo ayudarte?"):

    with st.chat_message("user"): #pintar el msj del usuario en el chat
        st.markdown(prompt) #responde con lo mismo que escribe el usuario
    st.session_state.messages.append({"role": "user", "content": prompt}) 

    result = chain.invoke({"business_info": info, "context": context, "question": prompt})

    with st.chat_message("assistant"): # Respondemos al usuario "assistant"
        st.markdown(result)   
    st.session_state.messages.append({"role": "assistant", "content": result}) 
    # añadimos a historico     

    context += f"Bot: {result}\nYou: {prompt}\n"  # Actualizamos el contexto para futuras preguntas


    # streamlit run front.py para ejecutar la app