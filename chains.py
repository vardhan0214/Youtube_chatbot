from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from retriever import retriever
from prompts import format_docs
from prompts import prompt
from models import model

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough()
})

# parallel_chain.invoke("Who is Demis")

main_chain = parallel_chain | prompt | model | parser

# result = main_chain.invoke("Can you summarize this video?")

# print(result)