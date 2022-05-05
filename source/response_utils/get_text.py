import re
from typing import Optional, Tuple


def get_text(message: str, author: str = None) -> Optional[Tuple[str, bool]]:
    response = {"text": None, "delete": False, "add_ok": False}
    regx = re.search(r"(?<=;ok)(~*)([\s\S]*)(?=;)", message, re.IGNORECASE)

    if regx is not None:
        if regx.group(1):
            if len(regx.group(1)) == 1:  # ok~
                response["delete"], response["add_ok"] = False, True
            elif len(regx.group(1)) == 2:  # ok~~
                response["delete"], response["add_ok"] = True, False
        else:
            response["delete"], response["add_ok"] = True, True

        response["text"] = regx.group(2)
        return response

    regx = re.search(r"([\s\S]*)bocie", message, re.IGNORECASE)

    if regx is not None:
        response["text"] = f"{regx.group(1)}{author}"
        return response

    regx = re.search(r"(kiedy|where) zdalne", message, re.IGNORECASE)

    if regx is not None:
        response[
            "text"
        ] = "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci"

    return response
