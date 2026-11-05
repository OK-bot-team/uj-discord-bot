from .random import randint
import re
from datetime import datetime


def get_text(message: str, author=None) -> dict[str, bool] | None:
    response = {"text": None, "delete": False, "add_ok": False, "image": False}

    if regx := re.search(r"(?<=;ok)(~*)([\s\S]*)(?=;)", message, re.IGNORECASE):
        if regx.group(1):
            if len(regx.group(1)) == 1:  # ok~
                response["delete"], response["add_ok"] = False, True
            elif len(regx.group(1)) == 2:  # ok~~
                response["delete"], response["add_ok"] = True, False
        else:
            response["delete"], response["add_ok"] = True, True

        response["text"] = regx.group(2)
        response["image"] = True
        return response

    if regx := re.search(r"([\s\S]*)bocie", message, re.IGNORECASE):
        response["text"] = f"{regx.group(1)}{author.display_name}"
        response["image"] = True
        return response

    if regx := re.search(r"(kiedy|where) zdalne", message, re.IGNORECASE):
        response[
            "text"
        ] = "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci"
        response["image"] = True
        return response

    if regx := re.search(r"(kiedy|where) zdalne", message, re.IGNORECASE):
        response[
            "text"
        ] = "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci"
        response["image"] = True
        return response

    if regx := re.search(r":deprecatedDelevoCry:", message):
        response[
            "text"
        ] = f"""----------
[{datetime.now().replace(microsecond = 0)}] WARNING: Deprecated emoji call.
<:deprecatedDelevoCry:917741279012610078> is deprecated.
{author.mention} please use the new <:baniaCry:1067860950700531842> cry emoji instead
----------"""
        return response

    if regx := re.search(r"\?", message):
        if randint(1, 400) >= 399:
            response[
                "text"
            ] = f"{author.mention} jako, że jesteś nowy to tym razem skończy się tylko na warnie ale w przyszłości UŻYJ OPCJI SZUKAJ, było wałkowane milion razy. Pozdrawiam, moderator forum."
            return response

    return None
