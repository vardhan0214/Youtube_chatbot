from langchain_ollama import ChatOllama, OllamaEmbeddings

model = ChatOllama(model = "llama3", temperature=0.2)
embedding_model = OllamaEmbeddings(model = "mxbai-embed-large")