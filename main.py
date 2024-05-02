from langchain_core.messages import HumanMessage

from src.chains import assistant_graph


def main() -> None:
    # while True:
    # user_input = input('Enter a message: ')

    output = assistant_graph.invoke([HumanMessage(content='test')])
    print(output)


if __name__ == '__main__':
    main()
