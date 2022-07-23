import requests


def get_request(url: str):
    try:
        response:requests.Response = requests.get(url)
        return response
    except requests.exceptions.Timeout:
        # change to custom error
        raise ValueError()


def abort_if_response_not_ok(response:requests.Response):
    if not response.ok:
        raise ValueError("invalid response")


def get_book_text(url:str, encoding:str) -> str:
    response = get_request(url)
    abort_if_response_not_ok(response)
    response.encoding = encoding
    text:str = response.text
    return text
