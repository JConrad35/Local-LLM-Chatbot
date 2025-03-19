from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = ChatPromptTemplate([
    ('system', 'You are a helpful AI assistant. Your name is {name}.'),
    ('human', 'Hello, how are you?'),
    ('ai', 'I am doing well, thank you. How can I help you today?'),
    ('human', '{user_input}')
])

prompt_value = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

chain = prompt_value | model

response = template.invoke(
    {
        'name': 'Juju',
        'user_input': 'What is your name?'
    }
)

print(response)
