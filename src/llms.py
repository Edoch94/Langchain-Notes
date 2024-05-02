from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableSequence

llm = ChatOllama(
    model='phi3',
    base_url='http://ollama:11434',
)


class ImpersonatorMessage(HumanMessage, AIMessage):
    @classmethod
    def from_ai_message(cls, ai_message: AIMessage) -> HumanMessage:
        ai_message_dict = ai_message.dict()
        ai_message_dict['type'] = 'human'
        print(ai_message_dict['content'])
        return cls(**ai_message_dict)


assistant = RunnableSequence(
    llm,
    ImpersonatorMessage.from_ai_message,
)
