from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config import OPENAI_API_KEY_1

from langchain_openai import ChatOpenAI as OpenAIRouterChatOpenAI

llm = OpenAIRouterChatOpenAI(
    model="qwen/qwen3-next-80b-a3b-instruct:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY_1,
)

def run_prompt(system_role: str, idea: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_role),
        ("human", "{idea}")
    ])
    chain = prompt | llm
    return chain.invoke({"idea": idea}).content