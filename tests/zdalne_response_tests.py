from source.response_utils.get_text import get_text

ZDALNE_ANSWER = "Nie ma żadnych zdalnych, zdalne wymyśliliście sobie Wy, studenci."

def no_response_test():
    assert get_text("zdalne") == (None, 0)
    assert get_text("kiedy") == (None, 0)
    assert get_text("where") == (None, 0)
    
def zdalne_and_bocie_response_test():
    assert get_text("kiedy zdalne bocie", "Holo, the Wisewolf") == ("kiedy zdalne Holo, the Wisewolf", 0)
    
def standard_zdalne_responses_test():
    assert get_text("kiedy zdalne") == (ZDALNE_ANSWER, 0)
    assert get_text("where zdalne") == (ZDALNE_ANSWER, 0)
    assert get_text("ale where zdalne") == (ZDALNE_ANSWER, 0)
    assert get_text("where zdalne i stacjonarne") == (ZDALNE_ANSWER, 0)