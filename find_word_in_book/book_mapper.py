from pathlib import Path
import json

PATH_TO_CONFIG = Path("find_word_in_book", "config.json")


def read_config_file(path_to_config):
    with open(Path(path_to_config)) as f:
        return json.load(f)


def get_possible_books():
    books = read_config_file(PATH_TO_CONFIG)
    return books

def map_book_name_to_url(book:str):
    books = get_possible_books()
    return books[book]


    