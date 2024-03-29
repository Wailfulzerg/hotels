import re


def to_snake_case(d: dict):
    def str_to_snake(s: str) -> str:
        return re.sub(r"([A-Z]\w+$)", "_\\1", s).lower()

    if isinstance(d, list):
        return [to_snake_case(i) if isinstance(i, (dict, list)) else i for i in d]
    return {
        str_to_snake(a): to_snake_case(b) if isinstance(b, (dict, list)) else b
        for a, b in d.items()
    }


def to_camel_case(d: dict):
    def str_to_camel_case(s: str) -> str:
        camel_string = "".join(x.capitalize() for x in s.lower().split("_"))
        return camel_string[0].lower() + camel_string[1:]

    if isinstance(d, list):
        return [to_camel_case(i) if isinstance(i, (dict, list)) else i for i in d]
    return {
        str_to_camel_case(a): to_camel_case(b) if isinstance(b, (dict, list)) else b
        for a, b in d.items()
    }
