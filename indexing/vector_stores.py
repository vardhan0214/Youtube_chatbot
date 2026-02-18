# Step 3 :>> Convert transcript splitted text into vectors and store them in a vector store

from langchain_community.vectorstores import FAISS
from models import embedding_model
from indexing.text_splitter import chunks

vector_store = FAISS.from_documents(chunks, embedding_model)

# print(vector_store.index_to_docstore_id)