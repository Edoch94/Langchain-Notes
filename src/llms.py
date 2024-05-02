from langchain_community.chat_models.ollama import ChatOllama

llm = ChatOllama(
    model='phi3',
    base_url='http://ollama:11434',
)
