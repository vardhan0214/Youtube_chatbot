from langchain_community.vectorstores import FAISS 
from indexing.vector_stores import vector_store

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# print(retriever)
# print(retriever.invoke('What is deepmind?'))

