from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from business_info import info

template = """
Answer the question below in Spanish.

Here is the business information:
{business_info} 

{context}

Question: {question}

Answer:

"""

model = OllamaLLM(model = "gemma3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def chat():
    print("Welcome to the chatbot")
    context = ""
    while True:
        question = input("You: ")
        if question == "stop":
            break

        result = chain.invoke({"business_info":info, "context": context, "question": question})
        print("Bot:", result)
        context += f"Bot: {result}\nYou: {question}\n"

if __name__ == "__main__":
    chat()      