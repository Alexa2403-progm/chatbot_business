# 🤖 Agente vitual "Chatbot" de eCommerce

### ⛓️‍💥 En este proyecto práctico se a creado un chatbot para negocios con inteligencia artificial, el modelo es descargado y corrido en local. Este modelo ya esta entrenado y le vamos a pasar la información del negócio para que responda al usuario preguntas específicas tanto de productos, metodos de pago, tiempos de entrega, etc.

## 🛠️ Instalación y Configuración

### 1️⃣ Clonar repositorio

```
git clone https://github.com/Alexa2403-progm/chatbot_business
```

### 2️⃣ Tener python instalado

### 3️⃣ instalar Ollama y luego descargar el modelo:
  
  ``` ollama
  ollama pull gemma3
  ```
Nos permite correr el LLMs en local, y para ejecutarlo:

```ollama
ollama run gemma3
```

### 4️⃣  instalar librerias

```
pip install -r requirements.txt
```

### 5️⃣ Por ultimo ejecuta 

```
streamlit run front.py
```
