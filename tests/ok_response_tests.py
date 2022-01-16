from source.response_utils.get_text import get_text

def no_response_test():
    assert get_text("") == (None, 0)
    assert get_text(" ") == (None, 0)
    assert get_text("A") == (None, 0)
    assert get_text("ok") == (None, 0)
    assert get_text("okser") == (None, 0)
    assert get_text("ok ser") == (None, 0)
    assert get_text("ok  ser") == (None, 0)
    assert get_text(";ok;") == (None, 0)
    assert get_text("; ok;") == (None, 0)
    assert get_text(";ok ;") == (None, 0)
    assert get_text("jakis tekst ;ok asdas;") == (None, 0)

def standard_ok_responses_test():
    assert get_text(";okser;") == ("ser", 0)
    assert get_text(";ok ser;") == (" ser", 0)
    assert get_text(";ok jakis dlugi tekst;") == (" jakis dlugi tekst", 0)
    assert get_text(";ok~abc;") == ("abc", 1)
    assert get_text(";ok~~abc;") == ("abc", 2)
    assert get_text(";ok~~~abc;") == ("abc", 3)