import os, sys
# add project root to path so logic_utils can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_message_too_high_says_go_lower():
    # When guess is too high, message must tell the player to go LOWER, not higher
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_message_too_low_says_go_higher():
    # When guess is too low, message must tell the player to go HIGHER, not lower
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
