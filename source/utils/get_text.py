import re


# returns text, number of escape symbols
# 0- delete original message
# 1- delete original and do not prepend "ok"
# 2- delete original and do not prepend "ok" nor emoji
# 3- do not delete and do not prepend "ok" nor emoji
def get_text(message, author=None):
    regx = re.search(r"(?<=;ok)(~*)([\s\S]*)(?=;)", message, re.IGNORECASE)

    if regx is not None:
        return regx.group(2), len(regx.group(1))

    regx = re.search(r"([\s\S]*) bocie", message, re.IGNORECASE)

    if regx is not None:
        return regx.group(1) + " " + author, 3

    regx = re.search(r"(kiedy|where) zdalne", message, re.IGNORECASE)

    if regx is not None:
        return "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci.", 3
    return None, 0
