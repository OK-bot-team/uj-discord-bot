from source.response_utils.get_text import get_text
import re


def test_get_text():
    text_none = ""
    assert get_text(text_none) == {
        "text": None,
        "delete": False,
        "add_ok": False,
        "image": False,
    }

    text_wrong = "abc"
    assert get_text(text_wrong) == {
        "text": None,
        "delete": False,
        "add_ok": False,
        "image": False,
    }

    text_1 = ";okabc;"
    assert get_text(text_1) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }
    text_2 = ";Okabc;"
    assert get_text(text_2) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_3 = ";oKabc;"
    assert get_text(text_3) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_4 = ";OKabc;"
    assert get_text(text_4) == {
        "text": "abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_5 = ";okabc ;"
    assert get_text(text_5) == {
        "text": "abc ",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_6 = ";ok abc;"
    assert get_text(text_6) == {
        "text": " abc",
        "delete": True,
        "add_ok": True,
        "image": True,
    }

    text_7 = "cześć bocie"
    author = "bejbe"
    assert get_text(text_7, author) == {
        "text": "cześć bejbe",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    text_8 = ";ok~abc;"
    assert get_text(text_8) == {
        "text": "abc",
        "delete": False,
        "add_ok": True,
        "image": True,
    }

    text_9 = ";ok~~abc;"
    assert get_text(text_9) == {
        "text": "abc",
        "delete": True,
        "add_ok": False,
        "image": True,
    }

    text_10 = ";ok~~~abc;"
    assert get_text(text_10) == {
        "text": "abc",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    text_11 = "bocie"
    assert get_text(text_11, "author") == {
        "text": "author",
        "delete": False,
        "add_ok": False,
        "image": True,
    }

    text_12 = ":deprecatedDelevoCry:"
    response = get_text(text_12)
    assert response["text"] is not None
    assert response["delete"] is False
    assert response["add_ok"] is False
    assert response["image"] is False
    assert re.search(r"WARNING: Deprecated emoji call",
                     response["text"]) is not None

    text_13 = ":DeprecatedDelevoCry:"
    response = get_text(text_13)
    assert response["text"] is None
    assert response["delete"] is False
    assert response["add_ok"] is False
    assert response["image"] is False
