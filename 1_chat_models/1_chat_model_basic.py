# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
# Load environment variables from .env
# load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")
model = OllamaLLM(model="llama3.1")
template = """Question: {question}

Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({"question": "What is 81 divided by 9?"})
# Invoke the model with a message
# result = model.invoke("")
print("Full result:")
print(result)
# print("Content only:")
# print(dir(result))
