# from models import model
# from prompts import final_prompt
from chains import main_chain

final_prompt = "Can you summarize this video?" 

answer = main_chain.invoke(final_prompt)
print(answer)
