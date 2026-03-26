# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI as OpenAIRouterChatOpenAI
# from config import OPENAI_API_KEY_1

# llm = OpenAIRouterChatOpenAI(
#     model="qwen/qwen3-next-80b-a3b-instruct:free",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=OPENAI_API_KEY_1,
# )


# def run_prompt(system_role: str, idea: str):
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", system_role),
#         ("human", "{idea}")
#     ])
#     chain = prompt | llm
#     a= chain.invoke({"idea": idea}).content
#     print(a)

import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "qwen/qwen3-next-80b-a3b-instruct:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)