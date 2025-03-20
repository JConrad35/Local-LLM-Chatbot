from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import os

# Function to search for files
def search_files(name, path = "C:\Users"): # might have to add a path to variable 'path'
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
            return result


# Chat Prompt Template
template = ChatPromptTemplate([
    ("system", 
     """"
     You are an ai assistant that helps users find files on their computer. These are your instructions:
        1. The user will provide you with a file name.
        2. You will search the user's computer for the file.
        3. If the file is found, you will return the file path.
        4. If the file is not found, you will let the user know.
     """),
    ("human", "Help me find the file {file_name}."),
    ("ai", "I can help you find the file {file_name}."),
    ("system", "Searching for file {file_name}."),
    ("ai", "I found the file '{file_name}' at the following path: {file_path}."),
    ("ai", "I'm sorry, I couldn't find the file '{file_name}'."),
    ("human", "Thank you."),
    ("ai", "You're welcome. Let me know if you need to find another file."),
])

model = OllamaLLM(model="llama3.2")

chain = template | model

chain.invoke({
    "file_name": "example.txt",
    "file_path": "C:/Users/username/Documents/example.txt"
})
