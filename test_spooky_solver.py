import pytest
import spooky_solver

@pytest.mark.parametrize("test_string, test_operation_and_value, output", [
    ("2spooky4me", "+1", "3spooky5me"),
    ("2spooky4me", "-1", "1spooky3me"),
    ("2spooky4me", "*2", "4spooky8me"),
    ("2spooky4me", "/2", "1spooky2me"),
    ("2spooky4me", "/100", "0spooky0me"),
    ("2spooky4me", "^2", "4spooky16me"),
    ("2spooky4me", "^3", "8spooky64me"),
    ("2", "+1", "3"),
    ("2", "-1", "1"),
    ("2", "*2", "4"),
    ("2", "/2", "1"),
    ("2", "/100", "0"),
    ("2", "^2", "4"),
    ("2", "^3", "8"),
    ("spooky", "+1", "spooky"),
    ("spooky", "-1", "spooky"),
    ("spooky", "*2", "spooky"),
    ("spooky", "/2", "spooky"),
    ("spooky", "/100", "spooky"),
    ("spooky", "^2", "spooky"),
    ("spooky", "^3", "spooky"),
    ("100spooky4me", "+1", "101spooky5me"),
    ("100spooky4me", "-1", "99spooky3me"),
    ("100spooky4me", "*2", "200spooky8me"),
    ("100spooky4me", "/2", "50spooky2me"),
    ("100spooky4me", "/100", "1spooky0me"),
    ("100spooky4me", "^2", "10000spooky16me"),
    ("1a2b3", "+1", "2a3b4"),
    ("a1b2c", "+1", "a2b3c"),
    ("1this2is3a4meme", "+1", "2this3is4a5meme"),
])
def test_main(test_string: str, test_operation_and_value: str, output: str):
    assert spooky_solver.main(['.\\spooky_solver.py', test_string, test_operation_and_value]) == output
