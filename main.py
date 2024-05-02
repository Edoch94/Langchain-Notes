from langchain_core.messages import HumanMessage

from src.chains import assistant_graph


def main() -> None:
    # while True:
    # user_input = input('Ask: ')
    user_input = 'Hi UNO, hi DUE, Edo here, how are you?'

    output = assistant_graph.invoke({'messages': [HumanMessage(content=user_input)]})
    # output = uno_chain.invoke([HumanMessage(content=user_input)])

    for message in output['messages']:
        print(message.pretty_print())


if __name__ == '__main__':
    main()
