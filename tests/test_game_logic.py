from logic_utils import check_guess, get_range_for_difficulty
#FIX: Refactored inital 3 tests to correctly test tuple output using Copilot Agent mode)
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert "Win" in result

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert "Too High" in result

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert "Too Low" in result

# LIMITATION: This test cannot call st.info() directly — Streamlit's UI layer does not
# run in pytest. Instead, we test the data that feeds into the info box string by calling
# get_range_for_difficulty and constructing the same f-string app.py uses. This will catch
# a broken get_range_for_difficulty function, but it will NOT catch a regression where
# someone re-hardcodes the string inside app.py itself while leaving this function correct.

def test_info_box_string_easy():
    # If difficulty is "Easy", range should be 1-20
    low, high = get_range_for_difficulty("Easy")
    info_text = f"Guess a number between {low} and {high}."
    assert "20" in info_text

def test_info_box_string_hard():
    # If difficulty is "Hard", range should be 1-50
    low, high = get_range_for_difficulty("Hard")
    info_text = f"Guess a number between {low} and {high}."
    assert "50" in info_text

def test_info_box_string_normal():
    # If difficulty is "Normal", range should be 1-100
    low, high = get_range_for_difficulty("Normal")
    info_text = f"Guess a number between {low} and {high}."
    assert "100" in info_text
