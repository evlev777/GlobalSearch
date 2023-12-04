from repository.parser.repository_parser import parser
from catalog.parser.catalog_parser import catalog_parser
from pyscript import document


def main_parser(user_str: str):
    if len(list(catalog_parser(user_str) + parser(user_str))) > 0:
        return list(catalog_parser(user_str) + parser(user_str))
    else:
        return 'Ничего не найдено. Проверьте свой запрос.'


def validator(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = english


if __name__ == '__main__':
    print(main_parser(input("Введите книгу:").strip().lower()))
