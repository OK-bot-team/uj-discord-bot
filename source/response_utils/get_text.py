from random import randint
import re
from typing import Optional, Dict
from datetime import datetime


def get_text(message: str, author=None) -> Optional[Dict[str, bool]]:
    response = {"text": None, "delete": False,
                "add_ok": False, "image": False}

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
        response["image"] = True
        return response

    regx = re.search(r"([\s\S]*)bocie", message, re.IGNORECASE)
    if regx is not None:
        response["text"] = f"{regx.group(1)}{author.display_name}"
        response["image"] = True
        return response

    regx = re.search(r"(kiedy|where) zdalne", message, re.IGNORECASE)
    if regx is not None:
        response[
            "text"
        ] = "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci"
        response["image"] = True
        return response

    regx = re.search(r"<:deprecatedDelevoCry:[0-9]*>", message)
    if regx is not None:
        response["text"] = f"----------\n[{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}] WARNING: Deprecated emoji call.\n <:deprecatedDelevoCry:917741279012610078> is deprecated.\n{author.mention} please use the new <:baniaCry:1067860950700531842> cry emoji instead.\n----------"
        return response

    regx = re.search(r"\?$", message, re.IGNORECASE)
    if regx is not None and randint(1, 400) >= 399:
        response["text"] = f"{author.mention} jako, że jesteś nowy to tym razem skończy się tylko na warnie ale w przyszłości UŻYJ OPCJI SZUKAJ, było wałkowane milion razy. Pozdrawiam, moderator forum."
        return response

    if randint(1, 4000) >= 3999:
        response["text"] = message + f" {author.display_name}"
        return response

    return None
