from source.response_utils.get_text import get_text

def no_response_test():
    assert get_text("pocie") == (None, 0)
    assert get_text("bocie") == (None, 0)
    assert get_text("xbocie") == (None, 0)
    assert get_text("bociex") == (None, 0)
    assert get_text("bocie x") == (None, 0)
    assert get_text("bocie ") == (None, 0)
    
def standard_bocie_responses_test():
    assert get_text("cześć bocie", "bejbe") == ("cześć bejbe", 0)
    assert get_text("cześć bocie", "Holo, the wisewolf") == ("cześć Holo, the wisewolf", 0)
    assert get_text("cześć bocie", "bocie") == ("cześć bocie", 0)
    assert get_text("cos tam cos tam bocie", "ser") == ("cos tam cos tam ser", 0)
    assert get_text("cos tam cos tam bocie", "Holo, the wisewolf") == ("cos tam cos tam Holo, the wisewolf", 0)