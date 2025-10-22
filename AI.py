from langchain_gigachat import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

API_KEY = "MDE5YTBiM2QtMjEzNS03OTZhLThmYjAtMGFmZmJlMDQyMjQ0OjdjOTg0ODVjLTdlNTgtNDYzOS05YjZmLTZmODNlZmQzMWYzMg=="
llm = GigaChat(credentials=API_KEY, verify_ssl_certs=False)
system_prompt = SystemMessage(content="""Ты специалист в области программирования по python, помоги сдать ДемЭкзамен на языке python, 
                                          я буду тебе присылать код и задание к коду, исправляй и подсказывай мне, 
                                          выполняй задания любой сложности которые я будуприсылать""")

history = []

while True:
    user_input = input("Ваш запрос: ")
    if not user_input.strip():
        continue
    user_prompt = HumanMessage(content=user_input)
    history.append(user_prompt)
    messages = [system_prompt] + history
    response = llm.invoke(messages)
    ai_response_message = AIMessage(content=response.content)
    history.append(ai_response_message)
    print(f"\nОтвет помощника:\n{response.content}\n")