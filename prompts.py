from langchain_core.prompts import PromptTemplate
from retriever import retriever

prompt = PromptTemplate(
    template = """
    You are a helpful assistant.
    Answer ONLY from the provided transcript context.
    If the context is insufficient, just say you don't know.

    {context}
    Question: {question}
""",
input_variables = ['context','question']
)



question = " is the topic of aliens discussed in this video? if yes then what was discussed"
# retrieved_docs = retriever.invoke(question)
# print(retrieved_docs)

# context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

# final_prompt = prompt.invoke({"context": context_text, "question": question})

# print(final_prompt)