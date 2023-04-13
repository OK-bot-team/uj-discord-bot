from source.response_utils.get_text import get_text
from source.response_utils.random import setNextInt
import re


def test_get_text():
    class Author:
        def __init__(self, name="author"):
            self.display_name = name

        def mention(self) -> str:
            return self.display_name

    text_none = ""
    setNextInt(0)
    assert get_text(text_none) is None

    text_wrong = "abc"
    setNextInt(0)
    assert get_text(text_wrong) is None

    text_randomMessage = "abc"
    author = Author()
    setNextInt(4000)
    assert get_text(text_randomMessage, author) == {
        "text": "abc author",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    text_lowercasePrintCommand = ";okabc;"
    assert get_text(text_lowercasePrintCommand) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }
    text_capitalizedPrintCommand = ";Okabc;"
    assert get_text(text_capitalizedPrintCommand) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_pokemonStylePrintCommand = ";oKabc;"
    assert get_text(text_pokemonStylePrintCommand) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_uppercaseOKPrintCommand = ";OKabc;"
    assert get_text(text_uppercaseOKPrintCommand) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_whitespaceOnEndOfPrintCommand = ";okabc ;"
    assert get_text(text_whitespaceOnEndOfPrintCommand) == {
        "text": "abc ",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_whitespaceInPrintCommand = ";ok abc;"
    assert get_text(text_whitespaceInPrintCommand) == {
        "text": " abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_bocieCommand = "cześć bocie"
    author = Author("bejbe")
    assert get_text(text_bocieCommand, author) == {
        "text": "cześć bejbe",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    text_singleTildePrintCommand = ";ok~abc;"
    assert get_text(text_singleTildePrintCommand) == {
        "text": "abc",
        "delete": False,
        "add_ok": True,
        "image": True,
    }

    text_doubleTildePrintCommand = ";ok~~abc;"
    assert get_text(text_doubleTildePrintCommand) == {
        "text": "abc",
        "delete": True,
        "add_ok": False,
        "image": True,
    }

    text_tripleTildePrintCommand = ";ok~~~abc;"
    assert get_text(text_tripleTildePrintCommand) == {
        "text": "abc",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    author = Author()

    text_standaloneBocieCommand = "bocie"
    assert get_text(text_standaloneBocieCommand, author) == {
        "text": "author",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    text_lowercaseWrongDeprecated = ":deprecatedDelevoCry:"
    response = get_text(text_lowercaseWrongDeprecated)
    assert response is None

    text_uppercaseWrongDeprecated = ":DeprecatedDelevoCry:"
    response = get_text(text_uppercaseWrongDeprecated)
    assert response is None

    text_noColonsWrongDeprecated = "deprecatedDelevoCry"
    response = get_text(text_noColonsWrongDeprecated)
    assert response is None

    text_correctDeprecated = "<:deprecatedDelevoCry:123456789>"
    author = Author()
    response = get_text(text_correctDeprecated, author)
    assert response["text"] is not None
    assert response["delete"] is False
    assert response["add_ok"] is False
    assert response["image"] is False
    assert (
        re.search(r"WARNING: Deprecated emoji call", response["text"])
        is not None
    )

    test_correctElektrodaHit = "pytanie?"
    setNextInt(400)
    author = Author()
    response = get_text(test_correctElektrodaHit, author)
    assert response["delete"] is False
    assert response["add_ok"] is False
    assert response["image"] is False
    assert (
        re.search(
            r"jako, że jesteś nowy to tym razem skończy się tylko na warnie ale w przyszłości UŻYJ OPCJI SZUKAJ, było wałkowane milion razy\. Pozdrawiam, moderator forum\.",
            response["text"],
        )
        is not None
    )

    test_correctElektrodaMiss = "pytanie?"
    setNextInt(0)
    author = Author()
    response = get_text(test_correctElektrodaMiss, author)
    assert response is None

    test_incorrectElektroda = "pytanie? "
    author = Author()
    response = get_text(test_incorrectElektroda, author)
    assert response is None
