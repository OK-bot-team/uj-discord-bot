from bot import get_text

def test_get_text():
    text_none = ""
    assert get_text(text_none) == None

    text_wrong = "abc"
    assert get_text(text_wrong) == None

    text_1 = ";okabc;"
    assert get_text(text_1) == "abc"

    text_2 = ";Okabc;"
    assert get_text(text_2) == "abc"

    text_3 = ";oKabc;"
    assert get_text(text_3) == "abc"

    text_4 = ";OKabc;"
    assert get_text(text_4) == "abc"

    text_5 = ";okabc ;"
    assert get_text(text_5) == "abc "

    text_6 = ";ok abc;"
    assert get_text(text_6) == " abc"
