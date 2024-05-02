from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableSequence
from langgraph.graph import END, MessageGraph

from src.llms import llm

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant named UNO'),
        MessagesPlaceholder(variable_name='messages'),
    ]
)

llm_chain = RunnableSequence(
    prompt,
    llm,
    StrOutputParser(),
)


def call_assistant(messages: list):
    return llm.invoke(messages)


graph = MessageGraph()

graph.add_node('assistant', call_assistant)
graph.add_edge('assistant', END)

graph.set_entry_point('assistant')

assistant_graph = graph.compile()
