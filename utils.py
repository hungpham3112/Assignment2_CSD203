import os


def clear():
    return os.system("cls")


def formatted_input(question: str = "") -> str:
    string = input(question).strip().upper()
    return string
