from bot import get_text

def test_get_text():
    text_none = ""
    assert get_text(text_none) == (None, 0)

    text_wrong = "abc"
    assert get_text(text_wrong) == (None, 0)

    text_1 = ";okabc;"
    assert get_text(text_1) == ("abc", 0)

    text_2 = ";Okabc;"
    assert get_text(text_2) == ("abc", 0)

    text_3 = ";oKabc;"
    assert get_text(text_3) == ("abc", 0)

    text_4 = ";OKabc;"
    assert get_text(text_4) == ("abc", 0)

    text_5 = ";okabc ;"
    assert get_text(text_5) == ("abc ", 0)

    text_6 = ";ok abc;"
    assert get_text(text_6) == (" abc", 0)

    text_7 = "cześć bocie"
    author = "bejbe"
    assert get_text(text_7, author) == ("cześć bejbe", 3)

    text_8 = ";ok~abc;"
    assert get_text(text_8) == ("abc", 1)

    text_9 = ";ok~~abc;"
    assert get_text(text_9) == ("abc", 2)

    text_10 = ";ok~~~abc;"
    assert get_text(text_10) == ("abc", 3)
