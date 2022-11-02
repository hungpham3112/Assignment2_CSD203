from engine import CustomerEngine, OrderingEngine, ProductEngine
from utils import clear


def display_base_menu():
    return """
1. Product 
2. Customer
3. Ordering
0. Quit
"""


def sub_menu(engine, question: str):
    inner = True
    while inner:
        clear()
        engine = engine
        print(engine.display_base_menu())
        stdin = input(question)
        clear()
        inner = engine.matching(stdin)
        clear()


def main():
    outer = True
    while outer:
        print(display_base_menu())
        stdin = input("Choose options (0-3): ")
        match stdin:
            case "1":
                sub_menu(ProductEngine(), "Choose options (0-9): ")
            case "2":
                sub_menu(CustomerEngine(), "Choose options (0-6): ")
            case "3":
                sub_menu(OrderingEngine(), "Choose options (0-3): ")
            case "0":
                outer = False
            case _:
                clear()
                continue


if __name__ == "__main__":
    main()
