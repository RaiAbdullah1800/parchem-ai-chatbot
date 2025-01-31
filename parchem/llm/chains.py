from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from .prompts import get_chat_prompt
import os

def initialize_chain():
    # Initialize LLM with OpenAI
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"), 
        model="gpt-4o-mini",
        temperature=0.7
    )
    
    # Create isolated memory buffer for each user
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        input_key="input"
    )
    
    # Create and return chain with memory
    return LLMChain(
        llm=llm,
        prompt=get_chat_prompt(),
        memory=memory,
        verbose=False
    )