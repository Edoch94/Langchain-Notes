import operator
from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnableSequence,
)
from langgraph.graph import END, StateGraph

from src.llms import assistant
from src.prompts import due_prompt, uno_prompt


def wrap_message_in_list(message: BaseMessage) -> Sequence[BaseMessage]:
    return [message]


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]


uno_chain = RunnableSequence(
    uno_prompt,
    assistant,
    RunnableParallel({'messages': RunnableLambda(wrap_message_in_list)}),
)

due_chain = RunnableSequence(
    due_prompt,
    assistant,
    RunnableParallel({'messages': RunnableLambda(wrap_message_in_list)}),
)


graph = StateGraph(AgentState)

graph.add_node('UNO', uno_chain)
graph.add_node('DUE', due_chain)

graph.add_edge('UNO', 'DUE')
graph.add_edge('DUE', END)

graph.set_entry_point('UNO')

assistant_graph = graph.compile()
