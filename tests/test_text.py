from bot import get_text

def test_get_text():
    text_none = ""
    assert get_text(text_none) == (None, False)

    text_wrong = "abc"
    assert get_text(text_wrong) == (None, False)

    text_1 = ";okabc;"
    assert get_text(text_1) == ("abc", False)

    text_2 = ";Okabc;"
    assert get_text(text_2) == ("abc", False)

    text_3 = ";oKabc;"
    assert get_text(text_3) == ("abc", False)

    text_4 = ";OKabc;"
    assert get_text(text_4) == ("abc", False)

    text_5 = ";okabc ;"
    assert get_text(text_5) == ("abc ", False)

    text_6 = ";ok abc;"
    assert get_text(text_6) == (" abc", False)

    text_7 = "cześć bocie"
    author = "bejbe"
    assert get_text(text_7, author) == ("cześć bejbe", True)
